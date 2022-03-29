sandwich_orders = [
    'egg sandwich',  
    'seafood sandwich',
    'roast beef sandwich', 
    'ham sandwich',
    'tuna sandwich'
]


finished_snadwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    
    print(f"I have made your {order.capitalize()}!")
    finished_snadwiches.append(order)

print("\nThe following are the finished sandwiches: ")

for sandwich in finished_snadwiches:
    print(sandwich)

print() 