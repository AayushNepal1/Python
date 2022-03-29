# Using tuples to store the immutable foods.
buffet_food = ('pizza', 'momo', 'chowmien', 'frenchfries', 'burger')

for food in buffet_food:
    print(food)

"""

    TypeError: 'tuple' object does not support item assignment
    buffet_food[0] = 'plain rice'
    print(buffet_food[0])

"""
print("\n")
buffet_food = ('pizza', 'momo', 'plain rice', 'alu jira', 'burger')
for revise_food in buffet_food:
    print(revise_food)