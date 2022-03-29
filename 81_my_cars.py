from .modules.car import Car
from .modules.electric_car import ElectricCar as EC

my_bettle = Car('volkswagen', 'bettle', 2019)
print(my_bettle.get_descriptive_name())

my_bettle.odometer_reading = 23
my_bettle.read_odometer()


my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

