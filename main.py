class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f'Color: {self.color}')


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
        self.width = side
        self.height = side
        self.side_length = side

    def side_length(self):
        return self.side_length


square = Square("Green", 8)
square.display_color()
print(square.width)
print(square.height)
print(square.side_length)
