class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Name:', self.restaurant_name, ', cuisine type:', self.cuisine_type)

    def open_restaurant(self):
        print('Reastaurant', self.restaurant_name, 'is open')


ris = Restaurant('Ris', 'Japanese')
mcdon = Restaurant('Mcdonalds', 'European')
varenik = Restaurant('Varenik', 'Russian')
ris.describe_restaurant()
mcdon.describe_restaurant()
varenik.describe_restaurant()
