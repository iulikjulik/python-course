import math

class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.area = math.pi * (self.radius ** 2)
        self.perimeter = 2 * math.pi * self.radius

circle = Circle(name="TestCircle", radius=5)
print(f'Circle: name={circle.name}, radius={circle.radius}, area={circle.area}, perimeter={circle.perimeter}')
