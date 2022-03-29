favorite_places = {
    'taudaha':[
        'anjan',
        'anish', 
        'cris'
    ],
    'chovar':[
        'pranjal',
        'rajeev', 
        'rishav'
    ],
    'hetauda':[
        'nishab',
        'biju', 
        'shivu'
    ],
}

for place, name in favorite_places.items():
    print(f"\n{place.title()} is the favorite place for: ")
    for guys in name:
        print(f"\t{guys.title()}")
print()