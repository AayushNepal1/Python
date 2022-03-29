prompt = "\nPlease enter the name of the city you have visited."
prompt +=  "\n(Enter 'quit' or 'Quit' or 'QUIT' or 'q' or 'Q' when you are done). "

while True:
    city = input(prompt)

    if city == 'quit' or city == 'q':
        break
    
    elif city == 'quit'.upper() or city == 'q'.upper():
        break
    
    elif city == 'quit'.capitalize():
        break
    
    else:
        print(f"I'd love to go to {city.title()}!")