persons = ['barsha', 'renuka', 'sushma']
print(f"I have invited {len(persons)} people for the dinner tonight.")
print("-----------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>>>> Previous invitation  list >>>>>>>>>>>>>>>>>>>")
print("-----------------------------------------------------------------")
print(f"Hello, {persons[0].title()} would like to have dinner with me.")
print(f"Hello, {persons[1].title()} would like to have dinner with me.")
print(f"Hello, {persons[-1].title()} would like to have dinner with me.")
print("-----------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>>>>> Out of the dinner list >>>>>>>>>>>>>>>>>>>>")
print("-----------------------------------------------------------------")
# removing the person who can't come to the dinner
busy = persons[0]
print(f"{busy.capitalize()} can't come to have a dinner with you.")
print("-----------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>>>> New dinner invitation list >>>>>>>>>>>>>>>>>>>")
print("-----------------------------------------------------------------")
# replacing the person who can't come to the dinner
persons[0] = 'Khusbhu'
print(f"Hello, {persons[0].title()} would like to have dinner with me.")
print(f"Hello, {persons[1].title()} would like to have dinner with me.")
print(f"Hello, {persons[-1].title()} would like to have dinner with me.")
print("-----------------------------------------------------------------")
# appending new dinner list
print("-----------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>>> New Guests list for dinner >>>>>>>>>>>>>>>>>>")
print("-----------------------------------------------------------------")
persons.insert(3 ,'anusha') 
persons.append('ritu') 
persons.append('manisha')
print(f"I have invited {len(persons)} people for the dinner tonight.")
print(f"Hello, {persons[0].title()} would like to have dinner with me.")
print(f"Hello, {persons[1].title()} would like to have dinner with me.")
print(f"Hello, {persons[2].title()} would like to have dinner with me.")
print(f"Hello, {persons[-3].title()} would like to have dinner with me.")
print(f"Hello, {persons[-2].title()} would like to have dinner with me.")
print(f"Hello, {persons[-1].title()} would like to have dinner with me.")
# shrinking the guest for the limited table spaces.
print("-----------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>> Guests removed  form the list  >>>>>>>>>>>>>>>>>")
print("-----------------------------------------------------------------")
print(f"Sorry,{persons.pop(0)} you can't come to the dinner tonight.")
print(f"Sorry,{persons.pop(2)} you can't come to the dinner tonight.")
print(f"Sorry,{persons.pop()} you can't come to the dinner tonight.")
print(f"Sorry,{persons.pop()} you can't come to the dinner tonight.")
# Now removing two from the dinner tonight.
print(persons)
del persons[0] 
print (persons)
del persons[0]
print(persons)