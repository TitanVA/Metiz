sandwich_orders = ['pastrami', 'meat', 'pastrami', 'cheese', 'fish', 'pastrami']
finished_sandwiches = []
print('Orders:', sandwich_orders)
print('Finished', finished_sandwiches)
print('Sorry but "pastrami" no more')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('Orders:', sandwich_orders)
print('Finished', finished_sandwiches)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your', sandwich, 'sandwich')
    finished_sandwiches.append(sandwich)

print('Orders:', sandwich_orders)
print('Finished', finished_sandwiches)
