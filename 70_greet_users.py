def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}..."
        print(msg)

usernames = ['aayush', 'anjan', 'rishav']
greet_users(usernames)