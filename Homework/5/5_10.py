current_users = ['viktor', 'sergey', 'vladimir', 'admin', 'anton']
new_users = ['viKtor', 'marina', 'ilya', 'Admin', 'albina']

for user in new_users:
    if user.lower() in current_users:
        print('User', user.title(), 'is already exist')
    else:
        print('Welcome', user.title())

