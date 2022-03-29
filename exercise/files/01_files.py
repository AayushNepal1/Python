filename = '/home/ubuntu/Desktop/python_works/exercise/files/text_data/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    contents.replace("python", "C")
    
print(contents)

print("-----------------------------------------------")

with open(filename) as file_object:
    for line in file_object:
        word = line.replace("python", "C")
        print(word.rstrip())


print("--------------------------------------------")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    word = line.replace("python", "C")
    print(word.strip())


