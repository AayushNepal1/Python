alien_0 = {'color': 'green', 'speed': 'slow'}

"""
Using keys in square brackets to retrieve the value you're interested in
from a dictionary might cause one potential problem: if the key you ask for
doesn't exist, you'll get an error.
"""
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
