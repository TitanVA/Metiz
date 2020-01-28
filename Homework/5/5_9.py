names = ['viktor', 'sergey', 'vladimir', 'admin', 'anton']
if names:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ', name.title(), ' thank you for logging in again', sep='')
else:
    print('We need to find some users!')
