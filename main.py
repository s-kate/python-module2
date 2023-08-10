class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Car: {self.make} {self.model}')


class Sedan(Car):
    def __init__(self, make, model, doors_count):
        super().__init__(make, model)
        self.doors_count = doors_count

    def display_info(self):
        super().display_info()
        print(f'Doors: {self.doors_count}')


class SUV(Car):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f'Seats: {self.seats}')


class SportsCar(Car):
    def __init__(self, make, model, max_speed):
        super().__init__(make, model)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f'Max speed: {self.max_speed} km/h')


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()
