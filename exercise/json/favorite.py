import json


filename = '/home/ubuntu/Desktop/python_works/exercise/json/fav_num.json'

try:
    with open(filename) as f:
        user =  json.load(f)
        print(f"I know your favorite number is {user}...!")
except FileNotFoundError:
    user = input("Enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(user, f)