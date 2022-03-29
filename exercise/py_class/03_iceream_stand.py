class Restaurant:
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_resturant(self):
        print(f"The name of the resturant is {self.resturant_name.title()}.")
        print(f"Available cuisine here is {self.cuisine_type.title()}.")

    def open_resturant(self):
        print(f"{self.resturant_name.title()} is open.")

    def read_customer(self):
        print(f"The served customers are: {self.number_served}.")
    
    def set_number_served(self, customer):
        if customer >= self.number_served:
            self.number_served = customer
        else:
            print("You can't take the order back from the customers.")

    def increment_number_served(self, additional):
        self.number_served += additional


class IceCreamStand(Restaurant):
    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavours = input("Enter the flavour of the icream you'd like to have: ")
        self.flavours = [self.flavours]

        
    def display_flavour(self):
        print(f"I'd love to have {self.flavours}-flavour icecream.")

my_icream = IceCreamStand('subbu', 'american')
my_icream.display_flavour()