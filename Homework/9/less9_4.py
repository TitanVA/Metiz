class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Name:', self.restaurant_name, ', cuisine type:', self.cuisine_type)

    def open_restaurant(self):
        print('Reastaurant', self.restaurant_name, 'is open')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def print_served(self):
        print('Served:', self.number_served)


ris = Restaurant('Ris', 'Japanese')
ris.print_served()
ris.set_number_served(15)
ris.print_served()
ris.increment_number_served(1)
ris.print_served()
