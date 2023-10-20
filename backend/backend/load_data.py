import logging
from pathlib import Path

import msgspec
from haversine import Unit, haversine
from pydantic_extra_types.coordinate import Coordinate

from models.restaurant import Restaurant


def read_restaurants_data(input_file: Path) -> list[dict]:
    msg = f"begin reading file {input_file.absolute()}"
    logging.info(msg)
    return_restaurants = msgspec.json.decode(input_file.open().read())
    msg = f"done reading file {input_file.absolute()} got\
          {len(return_restaurants)} restaurants"
    logging.info(msg)
    return return_restaurants["features"]


def from_geojson_to_restaurant_json(geojson_feature: dict) -> dict:
    # https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
    # use longitude latitude were pydantic
    # follow latitude longitude so we invert it here
    return {
        "id": geojson_feature["properties"]["full_id"],
        "name": geojson_feature["properties"]["name"],
        "coordinates": tuple(reversed(geojson_feature["geometry"]["coordinates"])),
    }


def from_restaurant_json_to_pydantic(restaurant_json: dict) -> Restaurant:
    return Restaurant.model_validate(restaurant_json)


if __name__ == "__main__":
    geojson_restaurants = read_restaurants_data(
        Path("../data") / "restaurants_paris.geojson",
    )
    restaurants = [
        from_restaurant_json_to_pydantic(
            from_geojson_to_restaurant_json(geojson_restaurant),
        )
        for geojson_restaurant in geojson_restaurants
    ]
    # latitude = float(input("latitude?\n"))
    # longitude = float(input("Longitude?\n"))
    # centroid = Coordinate(latitude, longitude)

    centroid = Coordinate(48.8319929, 2.3245488)
    radius = 100
    selected_restaurants = [
        restaurant
        for restaurant in restaurants
        if haversine(
            (restaurant.coordinates.latitude, restaurant.coordinates.longitude),
            (centroid.latitude, centroid.longitude),
            unit=Unit.METERS,
        )
        <= radius
    ]
    logging(len(selected_restaurants))
