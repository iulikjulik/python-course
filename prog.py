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
                print(f'Circle: name={shape.name} radius={shape.radius}, area={shape.area}, perimeter={shape.perimeter}')
            elif isinstance(shape, Triangle):
                print(f'Triangle: name={shape.name} area={shape.area}, perimeter={shape.perimeter}')
            elif isinstance(shape, Rectangle):
                print(f'Rectangle: name={shape.name} area={shape.area}, perimeter={shape.perimeter}')
        print('--------------------------------')
    
    def create(shape_type, shape_name):
        if shape_type == "circle":
            return Circle(name=shape_name)
        elif shape_type == "rectangle":
            return Rectangle(name=shape_name)
        elif shape_type == "triangle":
            return Triangle(name=shape_name)
        else: print("Unknown shape type.")
        return None

def main():
    def create(shape_type, shape_name):
        if shape_type == "circle":
            return Circle(name=shape_name)
        elif shape_type == "rectangle":
            return Rectangle(name=shape_name)
        elif shape_type == "triangle":
            return Triangle(name=shape_name)
        else: print("Unknown shape type.")
        return None

    shapes = Shapes()
    while True:
        command = input("Enter command (create, display, exit): ")
        if command == "create":
            shape_type = input("Enter shape type (circle, rectangle, triangle): ")
            shape = create(shape_type)
            if shape:
                shapes.add_shapes(shape)
        elif command == "display":
            shapes.display_shapes()
        elif command == "exit":
            break
        else:
            print("Unknown command.")
main()