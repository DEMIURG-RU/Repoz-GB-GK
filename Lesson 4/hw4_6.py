from itertools import count, cycle

def m_f(a, b, c):
    my_co = count(a)
    my_cy = cycle(b)
    for _ in range(c):
        print(f'Результат: {next(my_co)}, {next(my_cy)}')

a = int(input('Укажите число: '))
b = str(input('Введите строку: '))
c = int(input('Количество операций (ограничтель): '))

m_f(a, b, c)
