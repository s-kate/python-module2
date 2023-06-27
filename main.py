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

