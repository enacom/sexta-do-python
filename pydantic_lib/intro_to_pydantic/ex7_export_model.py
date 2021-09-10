"""Pydantic can convert a model instance to a dictionary, or json string"""
from pydantic_lib.utils import Movie

movie = Movie(title='Friday the 13th', year_of_release=1980, rating='R', box_office='U$93M')

movie_as_dict = movie.dict(exclude={'cast'})
movie_as_json = movie.json(exclude={'cast'})

print(movie_as_dict)
print(movie_as_json)
