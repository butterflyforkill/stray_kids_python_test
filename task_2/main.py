class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    circle = Circle(6, "blue")
    rectangle = Rectangle(3, 6, 'red')
    
    print(f"Rectangle area: {rectangle.area()}, Color: {rectangle.color}")
    print(f"Circle area: {circle.area()}, Color: {circle.color}")

    shapes = [rectangle, circle]
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.area()}")