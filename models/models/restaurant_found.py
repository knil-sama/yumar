from typing import Self

from pydantic import BaseModel, ValidationInfo, field_validator

from models.restaurant import Restaurant


class RestaurantFound(BaseModel):
    restaurant: Restaurant
    distance: float

    @field_validator("distance")
    def val_distance(self: Self, v: float, _: ValidationInfo) -> float:
        return round(v, 2)
