class Figure:
    count = 0 #클래스 변수(속성)

    #생성자
    def __init__(self, width, height):
        #객체(인스턴스) 변수 접근 예
        self.width = width 
        self.height = height

        Figure.count += 1
    
    def __del__(self):
        #클래스 변수 접근 예
        Figure.count -= 1

    #메서드
    def calc_area(self):
        return self.width * self.height #객체 변수 접근 예

figure1 = Figure(2,3)
print(Figure.count)
figure2 = Figure(2,3)
print(Figure.count) 

#클래스 변수: 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수
#           : 클래스 내외부에서 "클래스명.변수명"으로 엑세스 가능 

#인스턴스 변수: 클래스 정의에서 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는 변수
            #각 객체별로 서로 다른 값을 가짐
            #클래스 내부에선 self.인스턴스변수명을 사용해여 엑세서, 클래스 밖에서는 객체명.인스턴스변수명으로 엑세스