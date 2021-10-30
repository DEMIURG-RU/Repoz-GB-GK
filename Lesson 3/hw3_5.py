def sum_ch():
    v_ch = 0
    while True:
        add_l = input('Введите число или "q" для выхода: ').split()
        for numb in add_l:
            if numb.lower() == "q":
                return v_ch
            else:
                try:
                    v_ch += int(numb)
                except ValueError:
                    print("Для выхода из программы введите 'q': ")
                print(f'Сумма введеных вами чисел = {v_ch}')

print(f'Сумма всех введеных вами цифр равна {sum_ch()}')
