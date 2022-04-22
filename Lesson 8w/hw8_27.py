class MyErrDivByZero(Exception):
    def __init__(self, text):
        self.text = text

def div_num(a, b):
    try:
        a, b = int(a), int(b)
        if b == 0:
            raise MyErrDivByZero('Недопустимая операция - деление на ноль')
    except (ValueError, MyErrDivByZero) as err:
        print(err)
    else:
        return print(f'{a} / {b} = {a/b:.2f}')

print(div_num(input('Введите пеовое число: '), input('Введите второе число: ')))