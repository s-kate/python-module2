# class Vehicle

class Vehicle:

    def __init__(self, name: str, speed: int, cost: int):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed > other.speed


vehicles_list = [
    Vehicle("car", 120, 25000),
    Vehicle("motorcycle", 180, 15000),
    Vehicle("bike", 30, 1000),
    Vehicle("bus", 80, 50000)
]

speed_sorted_vehicles = sorted(vehicles_list, key=lambda v: v.speed)

for vehicle in speed_sorted_vehicles:
    print(f"{vehicle.name} - speed: {vehicle.speed} km/h")
