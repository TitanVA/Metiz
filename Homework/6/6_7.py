human = {
    'name': 'viktor',
    'surname': 'bezai',
    'age': 31,
    'city': 'krasodar'}

human2 = {
    'name': 'oleg',
    'surname': 'shah',
    'age': 24,
    'city': 'penza'
}

human3 = {
    'name': 'vova',
    'surname': 'hramch',
    'age': 35,
    'city': 'yakutsk'
}

people = [human, human2, human3]
print(people)
for person in people:
    print('\nFull name:', person['name'].title(), person['surname'].title())
    print('Age:', person['age'])
    print('From:', person['city'].title())
