class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print('Name:', self.first_name)
        print('Surname:', self.last_name)
        print('Age:', self.age)
        print('Sex:', self.sex)

    def greet_user(self):
        print('Welcome,', self.first_name.title(), self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print('Login attempts:', self.login_attempts)


viktor = User('viktor', 'bezai', '31', 'male')
viktor.print_login_attempts()
viktor.increment_login_attempts()
viktor.increment_login_attempts()
viktor.increment_login_attempts()
viktor.print_login_attempts()
viktor.reset_login_attempts()
viktor.print_login_attempts()
