# LESSON 2
# class Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimetr(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


rectangle1 = Rectangle(12, 5)
print(f'rectangle1 perimetr: {rectangle1.perimetr()}, area: {rectangle1.area()}')
