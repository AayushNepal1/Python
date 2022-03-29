name = ['Aayush', 'Anjan', 'Pranjal']

if 'Aayush' in name:
    print(f"My name is {name[0].title()}")

print()

country = 'England'

if country.lower() == 'england':
    print(country)
else:
    print("Can't compare")

print()


age = 18
if age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

print()


age_1 = 18
age_2 = 20

if age_1 <= 20 and  age_2 <= 20:
    print("You are less than or equal to 20 years old.")
else:
    print("You are more than 20 years old.")

print()

age_1 = 15
if age_1 >= 20 and age_2 >= 20:
    print(False)
else:
    print(True)

print()


if age_1 > 20 or age_2 < 21:
    print(False)
else:
    print(True)

print()

if 'Anish' not in name:
    print('Hello, sir you are not in the list to visit us.')

print()

