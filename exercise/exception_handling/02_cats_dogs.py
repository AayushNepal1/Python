def files(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        # print(f"File Not Found plase locate or create file please {filename}...")
        pass
        # This is used to hide the error from the program from the malicous threat

files('/home/ubuntu/Desktop/python_works/exercise/exception_handling/file_text/cats.txt')
#files('/home/ubuntu/Desktop/python_works/exercise/exception_handling/file_text/dogs.txt')
files('../file_text/dogs.txt')