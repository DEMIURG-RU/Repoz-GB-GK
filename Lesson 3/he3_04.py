def m_f(x, y):
    while y == 0:
        print('Попытка деления на ноль')
        return
    if y < 0:
        return f'Результат выражения: 1/(b_d**-n) равен {1 / pow(x, abs(y))}'
    y = float(input('Необходимо ввести отрицатльное число: '))
    return f'Результат выражения: 1/(b_d**-n) равен {1 / pow(x, abs(y))}'


xx = float(input('Введите любое действительное число: '))
yy = float(input('Введите любое отрицатльное число: '))

print(m_f(xx, yy))