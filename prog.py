import math
from circlerectangle import Circle
from circlerectangle import Rectangle
from triangle import Triangle

class Shapes:
    def __init__(self):
        self.shapelist = []
        self.file_path = "shapes.txt"
        self.load_shapes_from_file()
    
    def add_shapes(self, new_shape):
        self.shapelist.append(new_shape)
        self.save_shape_to_file(new_shape)

    def save_shape_to_file(self, shape):
        with open(self.file_path, 'a') as file:
            if isinstance(shape, Circle):
                file.write(f'circle,{shape.name},{shape.radius}\n')
            elif isinstance(shape, Triangle):
                file.write(f'triangle,{shape.name},{shape.area},{shape.perimeter}\n')
            elif isinstance(shape, Rectangle):
                file.write(f'rectangle,{shape.name},{shape.width},{shape.height}\n')

    def load_shapes_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    shape_type = data[0]
                    name = data[1]
                    if shape_type == "circle":
                        radius = float(data[2])
                        shape = Circle(name=name, radius=radius)
                    elif shape_type == "triangle":
                        area = float(data[2])
                        perimeter = float(data[3])
                        shape = Triangle(name=name, area=area, perimeter=perimeter)
                    elif shape_type == "rectangle":
                        width = float(data[2])
                        height = float(data[3])
                        shape = Rectangle(name=name, width=width, height=height)
                    self.shapelist.append(shape)
        except FileNotFoundError:
            pass

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

    def edit_shape(self, shape_name, new_attributes):
        for shape in self.shapelist:
            if shape.name == shape_name:
                if isinstance(shape, Circle):
                    shape.radius = new_attributes.get('radius', shape.radius)
                elif isinstance(shape, Triangle):
                    shape.area = new_attributes.get('area', shape.area)
                    shape.perimeter = new_attributes.get('perimeter', shape.perimeter)
                elif isinstance(shape, Rectangle):
                    shape.width = new_attributes.get('width', shape.width)
                    shape.height = new_attributes.get('height', shape.height)
                self.save_all_shapes_to_file()
                break

    def save_all_shapes_to_file(self):
        with open(self.file_path, 'w') as file:
            for shape in self.shapelist:
                self.save_shape_to_file(shape)

def main():
    shapes = Shapes()
    while True:
        command = input("Enter command (create, display, edit, exit): ")
        if command == "create":
            shape_type = input("Enter shape type (circle, rectangle, triangle): ")
            shape_name = input("Enter shape name: ")
            if shape_type == "circle":
                radius = float(input("Enter radius: "))
                shape = Circle(name=shape_name, radius=radius)
            elif shape_type == "rectangle":
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                shape = Rectangle(name=shape_name, width=width, height=height)
            elif shape_type == "triangle":
                area = float(input("Enter area: "))
                perimeter = float(input("Enter perimeter: "))
                shape = Triangle(name=shape_name, area=area, perimeter=perimeter)
            else:
                print("Unknown shape type.")
                continue
            shapes.add_shapes(shape)
        elif command == "display":
            shapes.display_shapes()
        elif command == "edit":
            shape_name = input("Enter the name of the shape to edit: ")
            new_attributes = {}
            attribute = input("Enter attribute to edit (radius, width, height, area, perimeter): ")
            value = float(input(f"Enter new value for {attribute}: "))
            new_attributes[attribute] = value
            shapes.edit_shape(shape_name, new_attributes)
        elif command == "exit":
            break
        else:
            print("Unknown command.")

main()
