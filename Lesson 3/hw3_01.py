def m_f(a, b):
    try:
        r_d = a / b
    except ZeroDivisionError:
        print(f'Ошибка - деление на 0')
        return
    return round(r_d, 2)
a = float(input('Введите значение 1-й переменной: '))
b = float(input('Ввелите значение 2-й переменной: '))
print(f'Результат деления 1-й переменной на вторую: {m_f(a, b)}')

