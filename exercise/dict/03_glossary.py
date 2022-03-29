from curses import keyname
from multiprocessing.sharedctypes import Value


glossary = {
    'list': 'List are mutable, ordered arrays which can store multiple values in a square brackets[].',
    'tuples': 'List are immutable, ordered arrays which can store multiple values in a parenthesis().',
    'dict': 'Dictonary are ordered arrays which can store the information on the key-value pair. To assign the dictonary we use curly braces {"\}".',
    'for_loops': 'The for in loops in python are can be use to access the values of various portion of data from list, tuples, dictionaries.',
    'conditional_statements': 'Their are various kind of the conditional statement. They can be used to test the whether the specified condition is true or false. If true then execute and if false then no execution.',
    'sets': 'Sets are unordered and unique which values are not repeated.To create the sets we use curly braces "{\}"',
    'print': 'The print function lets user to print the message on the console.',
    'keys()': 'The keys() method is used to access the keys from the dictionaries.',
    'Values()': 'The Values() methodd is used to access the values from the dictionaries.',
    'input()': 'The input() function only accepts the values as the string. To print the number taken from the input() function we can use type castings methods.',
}

# print(f"List: \n \t{glossary.get('list')}")
# print("\n")
# print(f"Tuples: \n \t{glossary.get('tuples')}")
# print("\n")
# print(f"Dictonary: \n \t{glossary.get('dict')}")
# print("\n")
# print(f"For Loops: \n t{glossary.get('for_loops')}")
# print("\n")
# print(f"Conditional Statement: \n \t{glossary.get('conditional_statements')}")

for title, meaning in glossary.items():
    print(f"\n{title}:\n \t{meaning}")
