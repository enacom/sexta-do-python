from datetime import date
from enum import Enum
from typing import Union, Optional, List

from pydantic import BaseModel, constr


class RatingEnum(str, Enum):
    G = 'G'
    M = 'M'
    R = 'R'


class Movie(BaseModel):
    title: str
    year_of_release: int
    rating: RatingEnum
    box_office: Union[float, str]
    cast: Optional[List[str]] = None


class User(BaseModel):
    name: constr(min_length=1)
    email: constr(regex=r'.+@.+\..+')
    birth_date: date
    favorite_movies: Optional[List[Movie]] = None
