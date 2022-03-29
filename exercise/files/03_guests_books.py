filename = '/home/ubuntu/Desktop/python_works/exercise/files/text_data/guest_books.txt'

active = True

prompt = "Enter Name: "

with open(filename, 'a') as file_object:
    while active:
        message = input(prompt)
        
        if message == 'q' or message == 'Q':
            active = False
            break
        else:
            file_object.write(f"Hello, {message}\n")