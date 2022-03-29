import json

filename =  'text_files/usernames.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
        for user in username:
            print(f"Welcome back , {user}!")
except FileNotFoundError:
    pass