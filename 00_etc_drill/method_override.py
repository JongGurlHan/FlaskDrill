class Car:
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        print(self.name)

class Eletronic_Car(Car):
    def get_info(self):
        print(self.name +" uses Eletronic")

class Gasoline_Car(Car):
    def get_info(self):
        print(self.name +" uses Gasoline")


new_electronic_car = Eletronic_Car("Teslar")
new_gasoline_car = Gasoline_Car("Porshe")

new_electronic_car.get_info()
new_gasoline_car.get_info()