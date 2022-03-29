users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'aayushnepal0011':{
        'first': 'aayush',
        'last': 'nepal',
        'location': 'taudaha',
    },
    'dbombal11':{
        'first': 'david',
        'last': 'bombal',
        'location': 'london',
    },
}


for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location.title()}")
