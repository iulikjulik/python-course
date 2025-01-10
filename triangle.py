import math


class Triangle:
    def __init__(self, side1, side2, side3, name):
        self.name = name
        self.side1 = side1 
        self.side2 = side2
        self.side3 = side3 
        s = (side1 + side2 + side3)/2
        self.area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
        self.perimeter = side1 + side2 + side3