import logging
from pathlib import Path

import click
import msgspec
from haversine import Unit, haversine
from pydantic_extra_types.coordinate import Coordinate

from models.restaurant import Restaurant
from models.restaurant_found import RestaurantFound
from models.search_query import SearchQuery


class NotAValidPointError(Exception):
    pass


def read_restaurants_data(input_file: Path) -> list[dict]:
    msg = f"begin reading file {input_file.absolute()}"
    logging.info(msg)
    return_restaurants = msgspec.json.decode(input_file.open().read())
    msg = f"done reading file {input_file.absolute()} got\
          {len(return_restaurants)} restaurants"
    logging.info(msg)
    return return_restaurants["features"]


def from_geojson_to_restaurant_json(geojson_feature: dict) -> dict:
    """_summary_

    Args:
        geojson_feature (dict): _description_

    Raises:
        NotAValidPointError: _description_

    Returns:
        dict: _description_
    """
    if geojson_feature["geometry"]["type"] != "Point":
        raise NotAValidPointError
    # https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
    # use (longitude, latitude) were our model
    # follow (latitude, longitude) so we invert it here
    return {
        "id": geojson_feature["properties"]["full_id"],
        "name": geojson_feature["properties"]["name"],
        "coordinate": tuple(reversed(geojson_feature["geometry"]["coordinates"])),
    }


def from_restaurant_json_to_pydantic(restaurant_json: dict) -> Restaurant:
    return Restaurant.model_validate(restaurant_json)


def search_restaurant(
    restaurants: list[Restaurant],
    search_query: SearchQuery,
) -> list[RestaurantFound]:
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


def load_data() -> list[Restaurant]:
    geojson_restaurants = read_restaurants_data(
        Path("../data") / "restaurants_paris.geojson",
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
    selected_restaurants = search_restaurant(restaurants, search_query)
    logging.warning(selected_restaurants)


if __name__ == "__main__":
    main()
