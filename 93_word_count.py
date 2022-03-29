# def banner(argument):
#     """Count the approximate number of words in a file."""
#     return argument

def count_words(filename):
    # print(banner.__doc__)
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        # This can be fail silently after failing
        # print(f"File Not Found. Please  create {filename}.")
        pass
    else:
        words = contents.split()
        num_words =  len(words)
        print(f"The file: {filename} has about {num_words} words.")


filename = ['text_files/alice.txt', 'text_files/bee_keeping_for_profit.txt', 'text_files/pi_digits.txt', 'hello.txt']


for file in filename:
    count_words(file)