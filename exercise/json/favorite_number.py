import json

prompt = "Enter your favorite number: "
filename = '/home/ubuntu/Desktop/python_works/exercise/json/fav_num.json'

with open(filename, 'w') as f:
    user = input(prompt) 
    user = int(user)
    json.dump(user, f)