from less9_4 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)

    def print_flavors(self):
        print('Flavors:', self.flavors)


IceCream = IceCreamStand('Morozko', 'Russian')
IceCream.add_flavors('mint', 'apple', 'strawberry')
IceCream.print_flavors()
IceCream.open_restaurant()