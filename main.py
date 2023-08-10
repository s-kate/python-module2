class Car:
    def __init__(self, make, model, year, mileage: int):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def drive(self, drive: int):
        if drive < 300000:
            self.mileage += drive
        else:
            print('you have reached the limit')

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())

car.drive(100)
print(car.get_mileage())
car.drive(300000)
