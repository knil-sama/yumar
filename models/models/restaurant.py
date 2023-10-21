from pydantic import (
    BaseModel,
)
from pydantic_extra_types.coordinate import Coordinate


class Restaurant(BaseModel):
    id: str  # noqa: A003
    name: str
    coordinate: Coordinate
