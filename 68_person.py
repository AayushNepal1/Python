def build_person(first_name, last_name,
age=None, occupation=''):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age and occupation:
        person['age'] = age
        person['occupation'] = occupation
    return person

full_name = build_person('aayush', 'nepal', age=19, occupation='programmer')
print(full_name)

for key, value in full_name.items():
    print(f"\n{key}: {value}")