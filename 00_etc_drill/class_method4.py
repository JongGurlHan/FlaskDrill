class Figure1:
    count = 0 #클래스 변수

    #생성자
    def __init__(self, width, height):
        
        #self.* : 인스턴스 변수
        self.width = width
        self.height = height
        
        # 클래스 변수 접근 예
        Figure1.count += 1

    #메서드
    def calc_area(self):
        return self.width * self.height
    
    #클래스 메서드
    #범위는 해당 클래스, 상속이 된다더라도 해당 클래스에 엑세스한다 
    @classmethod
    def print_count(cls): #인자가 없을때도 cls로 선언
        #print(self.width) 클래스 메서드도 객체속성, 메서드에 접근 불가 
        return cls.count #클래스 변수에 접근할 때도 cls.count
    
figure1 = Figure1(2,3)
figure2 = Figure1(4,5)

print(Figure1.count)
print(Figure1.print_count()) 
print(Figure1.print_count()) 
