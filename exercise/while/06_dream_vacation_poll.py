places = {}

active_polling = True

while active_polling:
    place = input("\nIf you could visit the place in a vacation which place do you prefer? ")
    fact = input("Why would you like to visit that place? ")

    places[place] = fact

    polling_repeat = input("Would you like to give a chance to your friends to take a poll(yes/  no)? ")
    
    if polling_repeat == 'no':
        active_polling = False

print("\n--- Polling Result ---")

for place, fact in places.items():
    print(f"I'd love to vist {place} because {fact}!")
print()