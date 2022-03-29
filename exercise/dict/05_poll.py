favorite_language = {
    'jen': 'python',
    'phil': 'java',
    'erik': 'c',
    'sarah': 'ruby',
    'mark': 'python',
}

friends = ['sarah', 'phil', 'aayush']

for name in sorted(favorite_language.keys()):
    print("Programming Languages mentioned:")

    if name in friends:
        print(f"\n{name.title()}, thanks for taking the poll.\n")
    
    if name not in friends:
        print(f"\n{name.title()}, please take the poll.\n")

print("Mentioned Language Are:")
for language in set(favorite_language.keys()):
    lang = favorite_language[language]
    print(lang)