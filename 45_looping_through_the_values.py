favorite_languages = {
    'anish': 'java',
    'aayush': 'python',
    'anjan': 'javascript',
    'cris': 'c',
    'rishav': 'python',
}


print("The following language are mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())

