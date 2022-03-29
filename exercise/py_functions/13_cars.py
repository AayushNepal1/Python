def make_car(name, manufacturer, **car_details):
    car_details['name'] = name
    car_details['manufacturer'] = manufacturer
    return car_details


car = make_car('bmw', 'bmw', color='black', seat='air bags', speed='300rpm', engine='boost')
for key, value in car.items():
    print(f"{key}: {value}")