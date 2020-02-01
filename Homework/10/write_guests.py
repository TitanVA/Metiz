with open('guests.txt', 'a') as wg:
    while True:
        guest = input('Enter your name or "q" to exit: ')
        if guest != 'q':
            print('Welcome', guest)
            wg.write(guest + '\n')
        else:
            break

with open('guests.txt', 'r') as wg:
    lines = wg.readlines()
    for guest in lines:
        print(guest, end='')
