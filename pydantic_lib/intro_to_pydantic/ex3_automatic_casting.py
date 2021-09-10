from pydantic import BaseModel, StrictInt


class MovieWhichAcceptsCasting(BaseModel):
    title: str
    year_of_release: int


class MovieWhichDoesNotAcceptCasting(BaseModel):
    title: str
    year_of_release: StrictInt


"""Pydantic will automatically cast '2019' to the integer 2019, unless the type is a StrictInt"""
movie_with_casting = MovieWhichAcceptsCasting(title='Parasite', year_of_release='2019')
print(movie_with_casting)

"""The next line will raise a validation error"""
movie_without_casting = MovieWhichDoesNotAcceptCasting(title='Parasite', year_of_release='2019')
print(movie_without_casting)
