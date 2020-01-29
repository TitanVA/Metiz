vacations = {}
print('--- A dream vacation ---')
running = True

while running:
    name = input('What\'s you name?\n')
    vacation = input('Where would you like to spend your vacation?\n')
    vacations[name] = vacation
    next_name = input('Would you like to add another man? (yes \ no),\
     or "list" to print list\n')
    if next_name == 'no':
        break
    elif next_name == 'list':
        for name, vacation in vacations.items():
            print('\n', name, 'would like to spend', vacation, '\n')

print('Results:')
for name, vacation in vacations.items():
    print(name, 'would like to spend', vacation)
