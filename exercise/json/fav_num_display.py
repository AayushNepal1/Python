import json

from json import JSONDecodeError

file = '/home/ubuntu/Desktop/python_works/exercise/json/fav_num.json'

try:
    with open(file) as f:
        user = json.load(f)
        print(f"I know your favorite number is {user}...!")
except JSONDecodeError:
    pass