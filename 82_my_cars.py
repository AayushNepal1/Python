from modules import car
from modules import electric_car

my_bettle = car.Car('volkswagen', 'bettle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
