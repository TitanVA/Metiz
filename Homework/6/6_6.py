favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

favorite_languages['alex'] = 'c++'
favorite_languages['taller'] = 'java'

new_users = {
    'oksana': 'c#',
    'viktor': 'python',
    'sarah': 'c'
}

for name, lang in favorite_languages.items():
    print(name.title(), 'like', lang.title(), 'language')

for name in new_users.keys():
    if name in favorite_languages:
        print('Hi', name.title())
    else:
        print(name.title(), 'come to our group')