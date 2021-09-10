"""
Python dataclasses do NOT validate type, whereas a pydantic BaseModel does
"""

from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic_lib.utils import RatingEnum


@dataclass
class MovieAsDataclass:
    title: str
    year_of_release: int
    rating: RatingEnum
    box_office: Union[float, str]
    cast: Optional[List[str]] = None


class MovieAsPydantic(BaseModel):
    title: str
    year_of_release: int
    rating: RatingEnum
    box_office: Union[float, str]
    cast: Optional[List[str]] = None


"""
Even though year_of_release should be an int, dataclasses will not raise an Exception if another type is provided
"""
bad_movie = MovieAsDataclass(title='The Room', year_of_release='Two thousand and three', rating=RatingEnum.R,
                             box_office="U$ 5M")
print(bad_movie)

"""
Pydantic, on the other hand will indicate the type error:
"""
bad_movie = MovieAsPydantic(title='The Room', year_of_release='Two thousand and three', rating=RatingEnum.R,
                            box_office="U$ 5M")
print(bad_movie)
