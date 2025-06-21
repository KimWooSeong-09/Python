class Car:
    def __init__(self, displ, drv):
        self.displ = displ
        self.drv = drv

    def Info(self):
        print(f'{self.displ}, {self.drv}구동')

car_obj = Car(3000, '4륜')
car_obj.Info()

