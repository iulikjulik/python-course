class Rectangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)
