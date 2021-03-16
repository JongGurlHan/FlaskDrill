class Figure:
    count = 0 #클래스 변수

    #생성자
    def __init__(self, width, height):
        self.width = width
        self.height = height

        Figure.count += 1
    
    def __del__(self):
        Figure.count -= 1

    #메서드
    def calc_area(self):
        return self.width * self.height
