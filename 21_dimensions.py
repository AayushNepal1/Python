# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""

TypeError: 'tuple' object does not support item assignment
dimensions[0] = 250 
print(dimensions[0])

"""

# A tuple with one element
my_t = (3, )
print(type(my_t))

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple
dimensions = (200, 50)
print("Orginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)