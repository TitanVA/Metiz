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
print('\nMore guests are coming!')
new = 'Antonio Banderas'
new2 = 'Anjelina Joly'
new3 = 'Bred Pitt'
guests.insert(0, new)
guests.insert(2, new)
guests.append(new3)
print(len(guests), 'guests come today:')
print(guests[0], ',', my_invite.lower(), sep='')
print(guests[1], ',', my_invite.lower(), sep='')
print(guests[2], ',', my_invite.lower(), sep='')
print(guests[3], ',', my_invite.lower(), sep='')
print(guests[4], ',', my_invite.lower(), sep='')
print(guests[5], ',', my_invite.lower(), sep='')
print(guests[6], ',', my_invite.lower(), sep='')
print('\nSorry only 2 guests today')
print(guests.pop(), 'sorry but you cant come')
print(guests.pop(), 'sorry but you cant come')
print(guests.pop(), 'sorry but you cant come')
print(guests.pop(), 'sorry but you cant come')
print(guests.pop(), 'sorry but you cant come')
print(guests[0], 'i\'l wait for you')
print(guests[1], 'i\'l wait for you')
del guests[0]
del guests[0]
print(guests)
