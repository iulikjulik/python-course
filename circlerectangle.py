class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.area = math.pi * (self.radius ** 2)
        self.perimeter = 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)
