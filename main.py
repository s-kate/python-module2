import math


class Circle:

    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = self.pi * math.sqrt(self.radius)
        return math.ceil(result)

    def lenght(self):
        result = 2 * self.pi * self.radius
        return math.ceil(result)


circle = Circle(5)
print(circle.area(), circle.lenght())
