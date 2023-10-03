"""

    03_class_attributes.py
    How attributes work at the class level

"""


class RaceCar:
    MAX_SPEED = 245
    ACCELERATION = 5

    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        self.speed += self.ACCELERATION
        if self.speed > self.MAX_SPEED:
            self.speed = self.__class__.MAX_SPEED


RaceCar.MAX_SPEED = 300
RaceCar.ACCELERATION = 50

car1 = RaceCar(245)
print(car1.speed)
car1.accelerate()
print(car1.speed)

car2 = RaceCar(270)
car2.accelerate()
print(car2.speed)


