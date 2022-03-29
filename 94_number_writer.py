import json

numbers = [2, 3, 5, 7, 11,13]

filename = 'text_files/numbers.json'
try:
    with open(filename, 'w') as f:
        json.dump(numbers, f)
        print(f"File created at the directory: {filename}")
        print("--------------------------------------------------------")
except FileNotFoundError:
    pass
else:
    try:
        with open(filename) as f:
            numbers = json.load(f)
            print("Here are the output of the json files: ")
            for num in numbers:
                print(num)
    except FileNotFoundError:
        pass