class Vehicles:
    def __init__(self, color):
        self.color = color
    def move(self):
        print("vehicles move")
class Car(Vehicles):
    def move(self):
        print("cars drive")
class Aeroplane(Vehicles):
    def move(self):
        print("aeroplanes fly")
vehicle1 = Car("pink") 
vehicle2 = Aeroplane("white")
vehicle1.move()
vehicle2.move()

        