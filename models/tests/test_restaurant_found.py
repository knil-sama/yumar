from models.restaurant import Restaurant
from models.restaurant_found import RestaurantFound


def test_RestaurantFound_round_distance():
    restaurant = Restaurant.model_validate(
        {"full_id": "", "name": "ssfsfd", "coordinates": (3.0, 3.0)}
    )
    restaurant_found = RestaurantFound(restaurant=restaurant, distance=0.314343434)
    # round properly
    assert 0.31 == restaurant_found.distance
