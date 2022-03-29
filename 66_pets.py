# A function with the positional arguments.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.!")

describe_pet(animal_type='cat', pet_name='solaart')
describe_pet(animal_type='dog', pet_name='jacky')
describe_pet(pet_name='jack', animal_type='mouse')
# describe_pet()

# A function with default Parameter
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.!")

describe_pet(pet_name='jackie')
describe_pet(pet_name='solankie',animal_type='cat')
describe_pet('bruno')
describe_pet('harry', 'hamster')
# describe_pet()

