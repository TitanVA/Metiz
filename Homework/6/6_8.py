poops = {
    'name': 'poops',
    'owner': 'viktor',
    'type': 'dog'
}

teddy = {
    'name': 'teddy',
    'owner': 'ilya',
    'type': 'cat'
}

jora = {
    'name': 'jora',
    'owner': 'maksim',
    'type': 'hamster'
}

pets = [poops, teddy, jora]
for pet in pets:
    print('\nPets name:', pet['name'])
    print('Owner:', pet['owner'])
    print('Pets type', pet['type'])
