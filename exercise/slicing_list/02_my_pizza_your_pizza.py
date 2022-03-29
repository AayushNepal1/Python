my_pizza = ['pepperoni', 'green peppers', 'mushrooms']
friend_pizza = my_pizza[:]
my_pizza.append('cheese pizza')
friend_pizza.append('onion pizza')
print("Here are my pizza that i have ordered:")
print(my_pizza)
print("\n")
print("Here are my firend pizza that he/she have ordered:")
print(friend_pizza)
print("\n")

print("My favorite pizza are:")
for pizza in my_pizza:
    print(pizza)
print("\n")

print("My friend favorite pizza are:")
for pizzas in friend_pizza:
    print(pizzas)
