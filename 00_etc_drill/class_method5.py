class Figure:
    @classmethod
    def set_name(cls, name):
        cls.name = name

class Circle(Figure):
    pass

Figure.set_name("figure")
print(Figure.name, Circle.name)

Circle.set_name("circle")
print(Figure.name, Circle.name)