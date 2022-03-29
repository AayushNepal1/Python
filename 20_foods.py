# copying a list

my_foods = ['pizza', 'momo', 'cake']
friend_foods = my_foods[:]

my_foods.append('carrot')
friend_foods.append('icecream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

for food in my_foods:
    print(food)
print("\n")

for foods in friend_foods:
    print(foods)
