from pydantic import AliasChoices, BaseModel, Field
from pydantic_extra_types.coordinate import Coordinate


class Restaurant(BaseModel):
    restaurant_id: str = Field(
        alias="id",
        validation_alias=AliasChoices("id", "full_id"),
    )
    name: str
    coordinate: Coordinate = Field(
        validation_alias=AliasChoices("coordinate", "coordinates"),
    )
