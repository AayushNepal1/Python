import json


def doc(argument):
    """
    \t\t.______________________.
    \t\t|                      |
    \t\t|   Greet the User     |
    \t\t|______________________|
    """
    return argument



def get_stored_username():
    """Get Stored UserNames if available."""
    filename = 'text_files/usernames.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your Name? ")
    
    filename = 'text_files/usernames.json'
    
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    
    return username


def greet_user():
    print(doc.__doc__)
    username = get_stored_username()
    if username in get_stored_username():
        prompt =  "Is the the correct user name? "
        user = input(prompt)
        if user == 'y'.lower() or user == 'y'.upper() and user == 'n'.lower() or user == 'n'.upper():
            print(f"Welcome back, {username}...!")
        else:
            username =  get_new_username()      
            print(f"We'll remember you when you come back, {username}!")
    # else:
    #     username = get_new_username()
    #     print(f"We'll remember you when you come back, {username}!")
    
greet_user()

