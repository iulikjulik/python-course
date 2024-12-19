class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius
        self.perimeter = 2 * 3.14 * radius


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = width * length
        self.perimeter = (width + length) * 2
