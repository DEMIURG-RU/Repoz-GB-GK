def gen_fact(num):
    v_ch = 1
    for i in range(num +1):
        yield f'{i}! = {v_ch}'
        v_ch *= i + 1

for ch in gen_fact(int(input('Введите число: '))):
#    print('Факторил числа и всех чисел входящих в него:')
    print(ch)
