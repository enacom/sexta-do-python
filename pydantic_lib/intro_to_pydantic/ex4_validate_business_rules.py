"""
Pydantic has constrained types (https://pydantic-docs.helpmanual.io/usage/types/#constrained-types) and a validator and
root_validator decorator for custom validation.
"""

from datetime import date, timedelta
from typing import List

from pydantic import BaseModel, constr, validator, root_validator

from pydantic_lib.utils import Movie, RatingEnum


class User(BaseModel):
    name: constr(min_length=1)  # Constrained str with one character minimum
    email: constr(regex=r'.+@.+\..+')  # Constrained str which must match given regular expression
    birth_date: date
    date_joined: date
    favorite_movies: List[Movie]

    @validator('birth_date', 'date_joined')  # validator decorator is used to validate specific fields
    def date_must_be_after_1900(cls, v):
        if v.year < 1900:
            raise ValueError('Cannot have date before year 1900')
        return v

    @root_validator  # root_validator has access to all fields, and can do cross validation
    def underage_user_cannot_have_r_rated_movie_as_favorite(cls, values):
        birth_date, favorite_movies = values.get('birth_date'), values.get('favorite_movies')
        age = (date.today() - birth_date) // timedelta(days=365.2425)
        if age < 18 and any([m.rating == RatingEnum.R for m in favorite_movies]):
            raise ValueError('User is too young (<18) to have R-rated movies in his favorite movies list')
        return values


# Next line will raise validation error because user is underage, and has R-rated movie as one of his favorites, and
# because date joined is before 1900
user = User(
    name='Underage User',
    email='underage@gmail.com',
    birth_date='2005-01-01',
    date_joined='1888-01-01',
    favorite_movies=[
        Movie(title='The Mitchells vs. The Machines',
              year_of_release=2021,
              rating=RatingEnum.G,
              box_office='-'),
        Movie(title='Joker',
              year_of_release=2019,
              rating=RatingEnum.R,
              box_office='U$1B'),
    ])

print(user)
