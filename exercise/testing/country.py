from module.city_function import loaction

print("Enter q to quit at any time")

while True:
    city = input("\nPlease tell the name of the city: ")
    if city == 'q':
        break
    country = input("\nPlease tell the name of the country: ")
    if country == 'q':
        break
    place = loaction(city,country)
    print(f"\nThe place I, want to visit is {place}")        
