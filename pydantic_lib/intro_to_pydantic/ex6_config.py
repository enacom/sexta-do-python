"""An internal config class can customize the way data is to be loaded -
https://pydantic-docs.helpmanual.io/usage/model_config/"""
from pydantic.main import BaseModel

from pydantic_lib.utils import snake_to_camel


class User(BaseModel):
    name: str
    email: str
    phone_number: str

    class Config:
        extra = 'ignore'
        '''
        There are 3 options for 'extra' field:
            1. Ignore: Ignores additional keys in data that do not have a corresponding key in model
            2. Allow: Allows additional keys, without validation
            3. Forbid: Raises error if data has extra keys
        '''
        alias_generator = snake_to_camel  # Maps key names as received by the data (dict/json/...) to field name


user_as_json = """{
    "name": "Newton",
    "email": "newton@enacom.com.br",
    "age": 28, 
    "phoneNumber": "91234-56789" 
}"""

# Extra field (age), will be ignored, since extra = 'ignore'
# Pydantic will convert camelCase (phoneNumber) to snake_case (phone_number)
user = User.parse_raw(user_as_json)
print(user)
