favorite_languages = {
    'anish': 'java',
    'aayush': 'python',
    'anjan': 'javascript',
    'cris': 'c',
}

friends = ['phil', 'aayush', 'salim', 'anish']

for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


if 'salim' not in favorite_languages.keys():
    print("Salim, please take your poll.")
