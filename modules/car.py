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
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
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


