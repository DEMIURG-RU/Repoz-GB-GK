class Stationery:
    def __init__(self, title='Чем будем рисовать'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать! {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} ручкой!')

class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} карандашом!')

class Marker(Stationery):
    def draw(self):
        print(f'Начинаем рисовать {self.title} маркером!')

start = Stationery()
pen = Pen('синей')
pencil = Pencil('простым')
marker = Marker('оранжевым')

office_sup = [start, pen, pencil, marker]

for i in office_sup:
    i.draw()


