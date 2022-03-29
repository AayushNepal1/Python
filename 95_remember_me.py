import json
users = []
prompt = "Press q or Q to quit the data storing process: "
print(prompt)
active = True
while active:
    username = input("What is your name: ")
    if username == 'q'.lower() or username == 'q'.upper():
        active = False
        break
    else:
        users.append(username)
        filename = 'text_files/usernames.json'
    
        with open(filename, "w+") as f:
           json.dump(users, f)
        for user in users:
            print(f"We'll remember you when you come back, {user}!")