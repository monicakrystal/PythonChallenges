class Vehicle:
    def __init__(self, seats, make, model, color, year):
        self.seats = seats
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def get_seats(self):
        return self.seats

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_year(self):
        return self.year

    def set_seats(self, seats):
        self.seats = seats

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def set_year(self, year):
        self.year = year

    def display_info(self):
        print(f"This car is a {self.color} {self.make} {self.model} with {self.seats} seats and made in {self.year}")