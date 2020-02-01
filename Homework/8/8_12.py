def sandwiches(*toppings):
    print('You ordered sandwich with:')
    for i in toppings:
        print('\t-', i)


sandwiches('cucumbers', 'sausage', 'tomatoes')
sandwiches('cheese', 'bacon')
