usernames = ['admin', 'aayush', 'anjan', 'pranjal', 'rishav']

for user in usernames:
    if 'admin' in user:
        print(f"Hello {user} would you like to see the status report?")
    else:
        print(f"\nHello {user} thank you for logging in again.")

print("\nSuccessfully generated the greeted all the users.")