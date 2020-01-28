favorite_places = {
    'viktor': ['bali', 'antalya', 'kiev'],
    'marina': ['kerch', 'kiev', 'tyrkey'],
    'ilya': ['sochi', 'krasnodar', 'oae']
}

for name, places in favorite_places.items():
    print('Favorite places of', name.title(), 'are:')
    for place in places:
        if place == 'oae':
            print('\t', place.upper())
        else:
            print('\t', place.title())

