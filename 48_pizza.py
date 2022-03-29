# store information about a pizza being order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order

print(f" You ordered a {pizza['crust']}-crust pizza " 
    "With the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)

    