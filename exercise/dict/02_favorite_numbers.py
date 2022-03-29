user_id = {
    'anish': [10, 30],
    'aayush': [11, 10],
    'anjan': [3, 25],
    'rajeev': [7, 10],
    'cris': [9, 10],
}

# anish = user_id['anish']
# aayush = user_id['aayush']
# anjan = user_id['anjan']
# rajeev = user_id['rajeev']
# cris = user_id['cris']

# print(f"Anish favorite number is {anish}.")
# print(f"Aayush favorite number is {aayush}.")
# print(f"Anish favorite number is {anjan}.")
# print(f"Rajeev favorite number is {rajeev}.")
# print(f"Cris favorite number is {cris}.")

for user, id in user_id.items():
    print(f"\n{user}'s favorite numbers are: ")
    for num in id:
        print(f"\t{num}")
    print(":::")
print()





