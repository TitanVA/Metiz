import random


age = random.randint(1, 80)
print(age)
if age < 2:
    print('baby')
elif 2 <= age <= 4:
    print('kid')
elif 4 <= age < 13:
    print('child')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('adult')
else:
    print('elderly')
