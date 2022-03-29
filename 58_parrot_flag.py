prompt = "\nTell me something, and I will repeat back to you."
prompt += "\nEnter quit or q or QUIT or Q or Quit to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit' or message == 'q':
        active = False
    
    elif message == 'quit'.upper() or message == 'q'.upper():
        active = False
    
    elif message == 'quit'.capitalize():
        active = False
    
    else:    
        print(message)
