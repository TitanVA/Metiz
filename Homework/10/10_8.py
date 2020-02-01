# with open('cats.txt', 'a') as cats:
#     name = input('Enter name of cat: ')
#     cats.write(name + '\n')
#
# with open('dogs.txt', 'a') as dogs:
#     name = input('Enter name of dog: ')
#     dogs.write(name + '\n')

try:
    with open('cats.txt', 'r') as cats:
        lines = cats.read()
        print(lines)
except FileNotFoundError:
    print('File not find')

try:
    with open('dogs.txt', 'r') as dogs:
        lines = dogs.read()
        print(lines)
except FileNotFoundError:
    print('File not find')
