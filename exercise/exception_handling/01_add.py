first_number = input("\nFirst Number: ")
second_number = input("\nSecond Number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    if str(first_number):
        message = f"You can't add {first_number} as a string and {second_number} as a number."
        print(message)
    elif str(second_number):
        message = f"You can't add {first_number} as number and {second_number} as a string."
        print(message.replace('string', 'number'))
else:
    print(answer)




