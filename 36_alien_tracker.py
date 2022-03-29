alien_0 = {'x_position': 0, 'y_poistion': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print(f"Orginal position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The nwe position is old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")