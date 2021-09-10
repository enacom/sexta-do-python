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


def snake_to_camel(field_name: str) -> str:
    """Convert snake_case to camelCase"""
    words = field_name.split('_')
    if len(words) < 2:
        return field_name
    first_word = words[0]
    other_words = words[1:]
    return first_word + ''.join(word.capitalize() for word in other_words)
