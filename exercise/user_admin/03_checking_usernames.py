current_users = [
        'AAYUSH', 'Anjan', 'rishav', 
        'anish', 'pranjal', 'cris', 'rajeev'
]

new_users = [
    'Aayush', 'david', 'keith chuck', 'anjan', 'chuck black'
]

available_user = current_users[:]

for new_user in new_users:
    if new_user in current_users:
        print(f"\n{new_user.title()} needs New UserName.")
    
    elif new_user.upper() in current_users:
        print(f"\n{new_user.title()} needs New User Name")
    
    elif new_user.capitalize() in available_user:
        print(f"\n{new_user.title()} needs New User Name")

    else:
        print(f"\n{new_user.title()} is available.")
    
