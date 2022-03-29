def documentation(argument):
    """This is a Open Source Program which counts the word in a text file"""
    return argument

def common_words(filename):
    print("-------------------------------------------------------------------")
    print(documentation.__doc__)
    print("-------------------------------------------------------------------")
    try:
        with open(filename) as f:
            contents = f.read()
            if contents.lower():
                line = contents.count('the ')
                print(line)
            if contents.upper():
                line = contents.capitalize().count('The ')
                print(line)
    except FileNotFoundError:
        pass


common_words('/home/ubuntu/Desktop/python_works/exercise/exception_handling/file_text/openSource.txt')

