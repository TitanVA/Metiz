class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print('Name:', self.first_name)
        print('Surname:', self.last_name)
        print('Age:', self.age)
        print('Sex:', self.sex)

    def greet_user(self):
        print('Welcome,', self.first_name.title(), self.last_name.title())


viktor = User('viktor', 'bezai', '31', 'male')
viktor.describe_user()
viktor.greet_user()
