pet_0 = {
    'animal': 'cat',
    'owner': 'aayush',
}
pet_1 = {
    'animal': 'dog',
    'owner': 'anjan',
}
pet_2 = {
    'animal': 'dog',
    'owner': 'pranjal',
}
pet_3 = {
    'animal': 'cat',
    'owner': 'siddhant',
}

pets = [pet_0,pet_1, pet_2, pet_3]


for pet in pets:
    for key, value in pet.items():
        print(f"\n{key}: {value}")
    print("---")
print()




