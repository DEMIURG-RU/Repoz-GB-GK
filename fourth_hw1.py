big_num = int(input('Введите длиное число : '))
ch = 0
while big_num > 0:
    ost_m = big_num % 10
    big_num //= 10
    if ost_m >= ch:
        ch = ost_m
        continue
print(ch)

