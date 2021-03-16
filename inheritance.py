class Figure:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Quadrangle(Figure):
    def set_area(self, width, height):
        self.width = width
        self.height = height

    def get_info(self):
        print(self.name, self.color, self.width, self.height)

square = Quadrangle('dave', 'blue')
square.set_area(5,5)
square.get_info()

print(issubclass(Quadrangle, Figure))