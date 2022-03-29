rivers = {
    'bagmati': 'nepal',
    'nile': 'egypt',
    'amazon': 'africa',
}


for river, country in rivers.items():
    print(f"\n{river.title()} runs through {country.title()}\n")


print("Name of the rivers mentioned:")

for river in rivers.keys():
    print(f"\n{river.capitalize()}\n")

print("Name of the countries mentioned:")

for country in rivers.values():
    print(f"\n{country.capitalize()}\n")
    