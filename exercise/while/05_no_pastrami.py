sandwich_orders = [
    'egg sandwich', 
    'pastrami', 
    'seafood sandwich',
    'pastrami', 
    'roast beef sandwich', 
    'ham sandwich',
    'pastrami', 
    'tuna sandwich'
]

finished_snadwiches = []

print("Deli has run rout of pastrami sandwich orders...!")

while sandwich_orders:
    order = sandwich_orders.pop()
    
    print(f"I have made your {order.capitalize()}!")
    finished_snadwiches.append(order)
    
    if 'pastrami' in finished_snadwiches:
        finished_snadwiches.remove('pastrami')

print("\nThe following are the finished sandwiches: ")

for sandwich in finished_snadwiches:
    print(sandwich.title())
print() 