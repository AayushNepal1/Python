cities = {
    'kathmandu':{
        'population': '1.442 million',
        'fact': "Kathmandu, Nepal's capital, is set in a valley surrounded by the Himalayan mountains.",
        'country': 'nepal'
    },
    'newyork':{
        'population': '8.419 million',
        'fact': "New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean.",
        'country': 'america'
    },
    'budapest':{
        'population': '1.756 million',
        'fact': "Budapest, Hungary’s capital, is bisected by the River Danube. Its 19th-century Chain Bridge connects the hilly Buda district with flat Pest. A funicular runs up Castle Hill to Buda’s Old Town, where the Budapest History Museum traces city life from Roman times onward.",
        'country': 'hungary'
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}: ")
    for key, value in info.items():
        print(f"\n{key}: {value}")
    print("---------------------------------")
print()

