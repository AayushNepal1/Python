from importlib.resources import contents


with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())