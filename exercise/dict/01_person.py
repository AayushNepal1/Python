user_0 = {
    'f_name': 'aayush',
    'l_name': 'nepal',
    'age': 19,
    'city': 'kathmandu',
}
user_1 = {
    'f_name': 'anjan',
    'l_name': 'nepal',
    'age': 20,
    'city': 'kathmandu',
}
user_2 = {
    'f_name': 'anish',
    'l_name': 'nepal',
    'age': 20,
    'city': 'kathmandu',
}

people = [user_0, user_1, user_2]

# f_name = user['f_name'].title()
# l_name = user['l_name'].title()
# age = user['age']
# city = user['city'].title()
# print(f"My name is {f_name} {l_name}, I am {age} years old and I live in {city}.")

for users in people:
    for key, value in users.items():
        print(f"\n{key}: {value}")
    print("...")
print()

