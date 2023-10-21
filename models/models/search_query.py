from typing import Annotated

from annotated_types import Gt
from pydantic import (
    BaseModel,
)
from pydantic_extra_types.coordinate import Coordinate

PositiveInt = Annotated[int, Gt(0)]


class SearchQuery(BaseModel):
    coordinate: Coordinate
    radius: PositiveInt
