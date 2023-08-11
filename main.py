from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def display_info(self):
        pass


class Sedan(Car):
    def __init__(self, make, model, doors_count):
        self.make = make
        self.model = model
        self.doors_count = doors_count

    def display_info(self):
        print(f'Car: {self.make} {self.model}\nDoors: {self.doors_count}')


class SUV(Car):
    def __init__(self, make, model, seats):
        self.make = make
        self.model = model
        self.seats = seats

    def display_info(self):
        print(f'Car: {self.make} {self.model}\nSeats: {self.seats}')


class SportsCar(Car):
    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed

    def display_info(self):
        print(f'Car: {self.make} {self.model}\nMax speed: {self.max_speed} km/h')


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()
