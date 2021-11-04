from random import choice

class Car:
    direction = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'Новая машина: {n} имеет цвет: {c}.\n Это полицейская машина? {p}')

    def go(self):
        print(f'{self.name}: Машина уехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась!')

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direction)}.')

    def sh_sp(self):
        return f'{self.name}: Скорость машины: {self.stop()}'

class TownCar(Car):

    def sh_sp(self):
        return f'{self.name}: Скорость машины: {self.speed}. Превышение!' if self.speed > 60 else super().sh_sp()

class WorkCar(Car):

    def sh_sp(self):
        return f'{self.name}: Скорость машины: {self.speed}. Превышение!' if self.speed > 40 else super().sh_sp()

class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p=True)

police_car = PoliceCar('"Полицейская"', 'белая', 80)
work_car = WorkCar('"Грузовая"', 'зеленая', 40)
town_car = TownCar('"Минивен"', 'черный', 65)
sport_car = SportCar('"Спортивная"', 'красная', 120)

list_of_cars = [police_car, work_car, town_car, sport_car]

for i in list_of_cars:
    i.go()
    print(i.sh_sp())
    i.turn()
    i.stop()
    print()





