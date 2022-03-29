players = ['charles', 'nadom', 'alice', 'cris', 'bruno']
print(players[0:3])
print()
print(players[1:4])
print()
# Omiting the first index
print(players[:4])
print()
# ommiting the last index
print(players[2:])
print()
# using the negative index
print(players[-3:])
print()
# Looping Through a Slice 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())