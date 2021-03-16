class nemo:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2

rectangle = nemo(10,5,"red")
square = nemo(7,7,"blue")

print(rectangle.get_area())
print(square.get_area())