filename = '/home/ubuntu/Desktop/python_works/exercise/files/text_data/polling.txt'

active_polling = True

prompt = "Why do you like programming: "

with open(filename, 'a') as file_object:
    while active_polling:
        message = input(prompt)
        
        redo = input("Enter would like to give a chance to other people?? ")
        
        if redo == 'n' or message == 'N':
            active = False
            break
        
        else:
            file_object.write(f"{message}\n")