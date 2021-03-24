class Figure:
    @classmethod
    def set_name(cls, name): #클래스 변수를 정의
        cls.name = name

class Circle(Figure):
    pass

Figure.set_name("figure")
print(Figure.name, Circle.name)

Circle.set_name("circle") #클래스 메소드의 범위는 해당 클래스 안!!!
print(Figure.name, Circle.name)

class Figure2:
    @staticmethod #클래스와는 별개의 함수
    def set_name(name): 
        Figure2.name = name

class Circle(Figure2):
    pass

Figure2.set_name("figure2")
print(Figure2.name, Circle.name)

Circle.set_name("circle")
print(Figure2.name, Circle.name)
