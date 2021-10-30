class Road:

    def __init__(self, widtht, lenght):
        self._lenght = lenght
        self._width = widtht

    def tot_wen_as(self, weight=25, thickness=5):
        return f'{self._width} m * {self._lenght} m * {weight} кг * {thickness} см = ' \
                f'{(self._width * self._lenght * weight * thickness) / 1000} т'

road_1 = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги в метрах: ')))
print(road_1.tot_wen_as())
