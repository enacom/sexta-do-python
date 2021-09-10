"""
Pydantic has constrained types (https://pydantic-docs.helpmanual.io/usage/types/#constrained-types) and a validator
decorator for custom validation.
"""

from datetime import date
from typing import List

from pydantic import BaseModel, constr, validator

from pydantic_lib.utils import Movie, RatingEnum


class User(BaseModel):
    name: constr(min_length=1)  # Constrained str with one character minimum
    email: constr(regex=r'.+@.+\..+')  # Constrained str which must match given regular expression
    birth_date: date
    date_joined: date
    favorite_movies: List[Movie]

    @validator('birth_date', 'date_joined')  # Field validator
    def date_must_be_after_1900(cls, v):
        if v.year < 1900:
            raise ValueError('Cannot have date before year 1900')
        return v


# Next line will raise validation error because of birth_date before 1900
user = User(name='Winston Churchill',
            email='church@gmail.com',
            birth_date='1874-11-30',
            date_joined='2000-01-01',
            favorite_movies=[
                Movie(title='The Great Dictator',
                      year_of_release=1940,
                      rating=RatingEnum.M,
                      box_office='U$ 4M'),
            ])
print(user)
