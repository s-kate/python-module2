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

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height

    def display_color(self):
        super().display_color()
        print(f'Width: {self.width}\nHeight: {self.height}')


rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()
