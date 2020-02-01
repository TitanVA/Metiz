print('Enter two numbers to add them:')
result = ''

while not result:
    try:
        a = int(input('First num: '))
    except ValueError:
        print('Enter int, not string')
        continue
    try:
        b = int(input('Second num: '))
    except ValueError:
        print('Enter int, not string')
        continue
    else:
        result = a + b
        print(result)
