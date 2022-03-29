from random import choice

number = [2, 5, 7, 9, 11, 17, 1, 10, 6, 4, 'a', 'n', 'm', 'l', 'k']

lottery = choice(number)
print(lottery)

if lottery == 11 or lottery == 7:
    print("You have won the lottery.")
elif lottery == 'a' or lottery == 'n':
    print("You have won the lottery.")
else:
    print("Beter luck :) next time.!!")

print("--------------------------------------")

print()

my_ticket = []

print("---------- Lottery Analysis -----------")

while len(number):
    if lottery != 11 or lottery != 7 or lottery != 'a' or lottery != 'n':
        my_ticket.append(number.pop())
        length = len(my_ticket)
        length += 1
        print((my_ticket))

print(f"The loop should run {length} times to give me winnig run.")