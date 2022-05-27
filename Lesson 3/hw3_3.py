def my_func(x, y, z):
    c_l = [x, y, z]
    c_l.remove(min(c_l))
    try:
        return f'Сумма наибольших значений в списке {sum(c_l)}'
    except TypeError:
        return "Пожалуйста вводите только числа"


print(my_func(-10, 12, 10))
