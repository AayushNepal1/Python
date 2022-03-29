age_prompt =  "Please enter your age, So that we'll set the correct pricing of the ticket: "
age_prompt += "Press q or Q to end the program: "

active = True

while active:
    message = input(age_prompt)
    
    if message == 'q' or message == 'quit':
        active = False
        break
    else:
        age = int(message)
        
        if age < 3:
            price = 0
    
        elif age < 12:
            price = 10
    
        else:
            price = 15
    
    print(f"\nThe cost of your move ticket is ${price}")

    