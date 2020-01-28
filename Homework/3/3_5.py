guests = ['Elon Musk', 'Albert Einstein', 'Nikola Tesla', 'Vasya Vakulenko']
my_invite = ' I\'d like to see you at dinner today!'
print(guests[0], ',', my_invite.lower(), sep='')
print(guests[1], ',', my_invite.lower(), sep='')
print(guests[2], ',', my_invite.lower(), sep='')
print(guests[3], ',', my_invite.lower(), sep='')
cant_came = guests.pop(0)
print(cant_came, 'cant came today.')
guests.insert(0, 'Matue Macconhy')
print(guests[0], ',', my_invite.lower(), sep='')
print(guests[1], ',', my_invite.lower(), sep='')
print(guests[2], ',', my_invite.lower(), sep='')
print(guests[3], ',', my_invite.lower(), sep='')
