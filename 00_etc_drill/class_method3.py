class Figure:
    count = 0  # 클래스 변수

    # 생성자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        # 클래스 변수 접근 예
        Figure.count += 1
        
    # 정적 메서드 (정적 메서드에서는 클래스 attribute 는 접근 가능)
    @staticmethod
    def print_count():
        print(Figure.count)

    # 정적 메서드 (에러: 정적 메서드에서는 객체 attribute 는 접근 불가)
    @staticmethod
    def print_width():
        print(self.width)
    
figure1 = Figure(1, 2)
print(Figure.count)
print(figure1.print_count())
print(figure1.print_width())