class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_or(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '-' * (self.nums % rows)

    def _str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сумма клеток: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Разница клеток: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше чем во второй'

    def __mul__(self, other):
        print('Умножение клеток: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Деление клеток: ')
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_or(7))

