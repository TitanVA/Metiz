toppings = []
run = True
while run:
    i = input('Enter topping for pizza, and type "quit" iif done: ')
    if i != 'quit':
        toppings.append(i)
    else:
        break

print('Your pizza with toppings:', toppings)
