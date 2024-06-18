from typing import List

from pydantic import BaseModel, conint


class BoardPoint(BaseModel):
    number: conint(ge=0, le=23)
    checkers_count: int
    occupied_by: str | None


class Board(BaseModel):
    bar_counts: dict
    points: List[BoardPoint]
