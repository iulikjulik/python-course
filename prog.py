import math
from circle import Rectangle
from circle import Circle
from triangle import Triangle
class Shapes:
    def __init__(self):
        self.shapelist = []
    def add_shapes(self, new_shape):
        self.shapelist.append(new_shape)
    def display_shapes(self):
        print('Current Shapes: ')
        for shape in self.shapelist:
            if isinstance(shape, Circle):
                print(f'Circle: radius={shape.radius}, area={shape.area}, perimeter={shape.perimeter}')
            elif isinstance(shape, Triangle):
                print(f'Triangle: area={shape.area}, perimeter={shape.perimeter}')
            elif isinstance(shape, Rectangle):
                print(f'Rectangle: area={shape.area}, perimeter={shape.perimeter}')
        print('--------------------------------')

def main():
    shapes = Shapes()

    shape1 = Circle(int(input('circle1 radius=')))
    shapes.add_shapes(shape1)
    shape2 = Circle(int(input('circle2 radius=')))
    shapes.add_shapes(shape2)
    shape3 = Triangle(int(input('side1=')), int(input('side2=')), int(input('side3=')))
    shapes.add_shapes(shape3)
    shape4 = Rectangle(int(input('rect width=')), int(input('rect length=')))
    shapes.add_shapes(shape4)


    shapes.display_shapes()
main()