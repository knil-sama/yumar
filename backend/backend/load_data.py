import logging
from functools import wraps
from pathlib import Path
from time import time

import click
import msgspec
from haversine import Unit, haversine
from pydantic_extra_types.coordinate import Coordinate

from models.restaurant import Restaurant
from models.restaurant_found import RestaurantFound
from models.search_query import SearchQuery


def timing(f):  # noqa: ANN201,ANN001
    @wraps(f)
    def wrap(*args, **kw):  # noqa: ANN202,ANN002,ANN003
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__!r} took: {te - ts:2.4f} sec")  # noqa: T201
        return result

    return wrap


class NotAValidPointError(Exception):
    pass


def read_restaurants_data(input_file: Path) -> list[dict]:
    """Open file and convert it to json

    Args:
        input_file (Path): Path of the restaurants file

    Returns:
        list[dict]: Restaurants list from the file
    """
    msg = f"begin reading file {input_file.absolute()}"
    logging.info(msg)
    return_restaurants = msgspec.json.decode(input_file.open().read())
    msg = f"done reading file {input_file.absolute()} got\
          {len(return_restaurants)} restaurants"
    logging.info(msg)
    return return_restaurants["features"]


def from_geojson_to_restaurant_json(geojson_feature: dict) -> dict:
    """Convert geojson features to simplified json restaurant

    Args:
        geojson_feature (dict): full restaurant description from geojson

    Raises:
        NotAValidPointError: Raised when we try to convert a no Point feature

    Returns:
        dict: A restaurant json that contain only
            full_id, name, coordinates (latitude, longitude)
    """
    if geojson_feature["geometry"]["type"] != "Point":
        raise NotAValidPointError
    # https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
    # use (longitude, latitude) were our model
    # follow (latitude, longitude) so we invert it here
    return {
        "full_id": geojson_feature["properties"]["full_id"],
        "name": geojson_feature["properties"]["name"],
        "coordinates": tuple(reversed(geojson_feature["geometry"]["coordinates"])),
    }


def from_restaurant_json_to_pydantic(restaurant_json: dict) -> Restaurant:
    """Convert simplified restaurant json to pydantic Restaurant type

    Args:
        restaurant_json (dict): A restaurant json that contain only
            full_id=> id, name, coordinate (latitude, longitude)

    Returns:
        Restaurant: pydantic representation
    """
    return Restaurant.model_validate(restaurant_json)


@timing
def search_restaurant(
    restaurants: list[Restaurant],
    search_query: SearchQuery,
) -> list[RestaurantFound]:
    """Do query spatial search on restaurant list

    Args:
        restaurants (list[Restaurant]): List of restaurants we are searching in
        search_query (SearchQuery): Query with a coordinate and a radius

    Returns:
        list[RestaurantFound]: List of restaurants that are
            in the perimeter of the search
    """
    return_found_restaurant = [
        RestaurantFound(restaurant=restaurant, distance=distance)
        for restaurant in restaurants
        if (
            distance := haversine(
                (restaurant.coordinate.latitude, restaurant.coordinate.longitude),
                (search_query.coordinate.latitude, search_query.coordinate.longitude),
                unit=Unit.METERS,
            )
        )
        <= search_query.radius
    ]
    # sort result from close to far, better user exp and help stabilize testing
    return_found_restaurant.sort(key=lambda x: x.distance)
    return return_found_restaurant


@timing
def load_data() -> list[Restaurant]:
    """Read restaurant file and convert content to python pydantic type

    Returns:
        list[Restaurant]: Restaurants from file
    """
    geojson_restaurants = read_restaurants_data(
        # could be done with env variable instead
        Path("../data")
        / "restaurants_paris.geojson",
    )
    return [
        from_restaurant_json_to_pydantic(
            from_geojson_to_restaurant_json(geojson_restaurant),
        )
        for geojson_restaurant in geojson_restaurants
    ]


@click.command()
@click.option("--latitude", type=click.FLOAT, help="latitude of search")
@click.option("--longitude", type=click.FLOAT, help="longitude of search")
@click.option("--radius", type=click.INT, help="radius of search")
def main(latitude: float, longitude: float, radius: int) -> None:
    search_query = SearchQuery(
        coordinate=Coordinate(latitude, longitude),
        radius=radius,
    )
    restaurants = load_data()
    found_restaurants = search_restaurant(restaurants, search_query)
    if found_restaurants:
        [
            print(found_restaurant)  # noqa: T201
            for found_restaurant in found_restaurants
        ]
    else:
        print("No restaurants found")  # noqa: T201


if __name__ == "__main__":
    main()
