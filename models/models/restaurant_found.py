from typing import Self

from pydantic import BaseModel, ValidationInfo, field_validator

from models.restaurant import Restaurant


class RestaurantFound(BaseModel):
    restaurant: Restaurant
    distance: float

    @field_validator("distance")
    def val_distance(cls, v: float, _: ValidationInfo) -> float:  # noqa: ANN101, N805
        return round(v, 2)

    def __str__(self: Self) -> str:
        return f"name: {self.restaurant.name}, \
longitude:{self.restaurant.coordinate.longitude}, \
latitude:{self.restaurant.coordinate.latitude}, \
distance:{self.distance}"
