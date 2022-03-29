number = input("Enter a number, and I'll tell you whether the numer is multiples of 10 or not? ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is multiple of 10.")
else:
    print(f"The number {number} is not multiple of 10.")