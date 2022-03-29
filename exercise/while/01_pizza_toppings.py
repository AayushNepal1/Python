toppings = []

message = ""

prompt = "\nPlease place your order:"
prompt += "Please press quit or q to end your order. "

while message != 'quit' and message != 'q':
    message = input(prompt)
    
    toppings.append(message)
        
    for topping in toppings:
        if topping == 'quit' or topping == 'q':
            break
        else:
            print(f"I'll add that topping {topping} pizza to the order list.")
    print()
        