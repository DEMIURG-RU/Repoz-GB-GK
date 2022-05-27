class ComplNum:
    def __init__(self, c_n1):
        self.c_n1 = c_n1

    def __add__(self, other):
        return self.c_n1 + other.c_n1

    def __mul__(self, other):
        return self.c_n1 * other.c_n1

def check_gen(x, y):
    a_1, a_2, b_1, b_2 = x.real, x.imag, y.real,y.imag
    print(complex((a_1+b_1), (a_2+b_2)),complex(((a_1*b_1)-(a_2*b_2)), ((a_2*b_1)+(a_1*b_2))))

a = complex(input('Введите первое комплексное число: '))
b = complex(input('Введите второе комплексное число: '))
coll_1, coll_2 = ComplNum(a), ComplNum(b)
print(a+b, a*b)
check_gen(a, b)