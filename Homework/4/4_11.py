pizzas = ['pepperoni', 'margarita', 'four cheeses']
for pizza in pizzas:
    print('I like ', pizza, ' pizza', sep='')
print('I really love pizza!')
friend_pizzas = pizzas[:]
pizzas.append('meaty')
friend_pizzas.append('seafood')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
