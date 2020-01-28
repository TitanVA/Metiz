cities = {
    'krasnodar': {
        'country': 'russia',
        'population': 1200000,
        'fact': 'it\'s very hot in here'
    },
    'kiev': {
        'country': 'ukraine',
        'population': 3500000,
        'fact': 'it\'s capital of Ukraine'
    },
    'minsk': {
        'country': 'belarus',
        'population': 2700000,
        'fact': 'it\'s capital of Belarus'
    },
}

for city, infos in cities.items():
    print('City\'s name:', city)
    for info in infos.keys():
        if info == 'country':
            print('Country of city: ', infos[info])
        if info == 'population':
            print('Population are:', infos[info])
        if info == 'fact':
            print('Fact of city:', infos[info])
