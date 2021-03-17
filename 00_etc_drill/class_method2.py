# instance method: 해당 객체 안에서만 호출, 동작한다 
# class method: 해당 클래스 만을 범위로 한다 
# static method: class와 instance메소드의 범위를 넘어선다 
#               :static method는 부모, 자식 클래스가 있을때  부모,자식 상관없이 전체를 범위로 가진다.  
# 객체와 독립적이지만 로직상 클래스 내에 포함된다, 일종의 함수인데, 클래서 안에서 정의되는 함수로 이해
# static method는 메서드 앞에 @staticmethod라는 Decorator를 넣어야함 

class Figure:
    #생성자
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    #객체 메서드, instance method
    def calc_area(self):
        return self.width * self.height
    
    #정적 메서드, static method(Figure에 너비와 높이가 같은 도형은 정사각형임을 알려주는 기능)
    #클래스를 생성하든 안하든 Figure.해당 메서드 명 으로 호출할 수 있다., 보통 클래스명.정적메서드로 호출하는게 일반적이다 
    @staticmethod
    def is_square(rect_width, rect_height):
        if rect_width == rect_height:
            print("정사격형이 될 수 있는 너비/높이입니다.")
        else:
            print("정사격형이 될 수 없는 너비/높이입니다.")

figure1 = Figure(2,3)
figure1.is_square(5,5)
Figure.is_square(5,3)

#정적메소드는 클래스 안에 있지만, 클래스와 분리된 일종의 함수라고 생각하면 된다 
#이렇게 분리되어있기에 객체 속성에 접근할 수 없다. 