prompt = "\nTell me something, and I will repeat back to you."
prompt += "\nEnter quit to end the program. "

message = ""

while message != 'quit' and message != 'q':
    message = input(prompt)

    if message != quit:
        print(message)
