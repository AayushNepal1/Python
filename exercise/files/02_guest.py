filename = '/home/ubuntu/Desktop/python_works/exercise/files/text_data/guest.txt'


with open(filename, 'w') as file_object:
    guest = input("Enter the name of the guests: ")
    file_object.write(guest)