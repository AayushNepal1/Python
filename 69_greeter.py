def get_formatted_name(first_name, last_name):
    """Return a dictionary of information about a person."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop !
while True:
    print("\nPlease tell me your name:")
    print("\nPlease enter q or Q to quit at any time:")
    f_name = input("First Name: ")
    if f_name == 'q' or f_name == 'q'.upper():
        break
    l_name = input("Last Name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")


