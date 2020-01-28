import random


num = random.randint(1,10)
print('Random num is:')
if num == 1:
    print(num, 'st', sep='')
elif num == 2:
    print(num, 'nd', sep='')
elif num == 3:
    print(num, 'rd', sep='')
else:
    print(num, 'th', sep='')

print('\nRange numbers:')
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print(num, 'st', sep='')
    elif num == 2:
        print(num, 'nd', sep='')
    elif num == 3:
        print(num, 'rd', sep='')
    else:
        print(num, 'th', sep='')
