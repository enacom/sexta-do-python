"""Pydantic will raise just one validation error for the model, but within it is a list of all errors that occurred"""
from datetime import date

from pydantic import BaseModel, constr, validator, ValidationError, PydanticValueError


class BadDateError(PydanticValueError):
    msg_template = 'Cannot have date before year 1900.'


class User(BaseModel):
    name: constr(min_length=1)
    email: constr(regex=r'.+@.+\..+')
    birth_date: date
    date_joined: date

    @validator('birth_date', 'date_joined')
    def birth_date_must_be_after_1900(cls, v):
        if v.year < 1900:
            raise BadDateError()
        return v


# User has invalid name, email, birth date and date joined. ValidationError contains all 4 of these errors
try:
    bad_user = User(name='', email='bad_email', birth_date='1800-01-01', date_joined='1899-12-31')
except ValidationError as e:
    list_of_errors = e.errors()
    print(e.json())
