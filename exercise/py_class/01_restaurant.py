from modules.resturant import Restaurant

restaurant = Restaurant('subbu', 'nepali')
print(f"The name of the resturant is {restaurant.resturant_name.title()}.")
print(f"Avalible cuisine is {restaurant.cuisine_type.title()}.")
restaurant.describe_resturant()
restaurant.open_resturant()

print("--------------------------------------------")

restaurant = Restaurant('ruby red', 'chinese')
print(f"The name of the resturant is {restaurant.resturant_name.title()}.")
print(f"Avalible cuisine is {restaurant.cuisine_type.title()}.")
# Modifying the attribute's value through a method
restaurant.describe_resturant()
restaurant.set_number_served(25)
restaurant.read_customer()
restaurant.increment_number_served(100)
restaurant.read_customer()
print("----------------------------------------------")

restaurant = Restaurant('universal cafe', 'italian')
print(f"The name of the resturant is {restaurant.resturant_name.title()}.")
print(f"Avalible cuisine is {restaurant.cuisine_type.title()}.")
# Modifying the attribute's value directly
restaurant.number_served = 20
print(f"The resturant have serverd {restaurant.number_served} customers.")
restaurant.describe_resturant()


