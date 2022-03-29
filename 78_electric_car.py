class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descripted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        "Print a statement showing the car's mileage."
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an attribute's value through a method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # Increment an attribute's value through method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles   

    def fill_gas_tank(self):
        print("..... Filling the gas tank full ......")


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
    
 
    def get_range(self):
        """Print a statement about the range this battery provide."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315


        print(f"This car can go about {range} miles on a full charge.")    
    

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vechile."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 75

        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car don't have a gass tank"""
        print("This car doesn't need a gas tank.")
    
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
