names = {'viktor': [8, 9],
         'marina': [7, 5],
         'polya': [9, 2],
         'ilya': [2, 18],
         }
for name, nums in names.items():
    print(name.title(), 'like number\'s:', end=' ')
    for num in nums:
        print(num, end=', ')
    print('')
