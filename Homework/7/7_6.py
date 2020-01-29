age = 0
running = True

while running:
    age = input('Enter your age or "quit" for exit: ')
    if age != 'quit':
        if int(age) < 3:
            print('Your price: "free"')
        elif int(age) < 12:
            print('Your price: 10$')
        else:
            print('Your price: 15$')
    else:
        break
