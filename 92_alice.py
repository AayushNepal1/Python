filename ='text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File can't be read. Please create the file {filename}:::")
else:
    # Count the approximate number of words in a file.
    words = contents.split()
    num_words = len(words)
    print(f"The file: {filename} has about {num_words} words.")

