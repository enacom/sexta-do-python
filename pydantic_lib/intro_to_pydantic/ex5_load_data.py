"""Pydantic has methods to load data from dictionaries, strings or files"""
from pydantic_lib.utils import User

user_as_dict = {
    'name': 'Gustavo',
    'email': 'gustavo@enacom.com.br',
    'birth_date': '2001-01-01',
    'favorite_movies': [
        {
            'title': 'Pelé',
            'year_of_release': 2021,
            'rating': 'G',
            'box_office': '-'
        }
    ]
}

user_as_json_str = '''
{
    "name": "Gustavo",
    "email": "gustavo@enacom.com.br",
    "birth_date": "2001-01-01",
    "favorite_movies": [
        {
            "title": "Pelé",
            "year_of_release": 2021,
            "rating": "G",
            "box_office": "-"
        }
    ]
}
'''

user_1 = User.parse_obj(user_as_dict)
user_2 = User.parse_raw(user_as_json_str)
user_3 = User.parse_file('../utils/example_user.json')

print(user_1)
print(user_2)
print(user_3)
