magicans = ['Leonardo', 'Davinchi', 'Alex', 'Mikel']


def show_magicans(magicans):
    for magican in magicans:
        print(magican)


def make_great(magicans):
    for i in range(len(magicans)):
        magicans[i] = 'Great ' + magicans[i]
    show_magicans(magicans)


make_great(magicans[:])

print(magicans)
