from less9_5 import User


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять пользователей',
                           'разрешено банить пользователей']

    def show_privileges(self):
        print('You have priveleges:', self.privileges)



