months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
type(months)
print(months)
num_mo = int(input('Введите число месяца (от 1 до 12): '))
if months[num_mo-1] <= 2 or months[11] == num_mo:
    print(f'Это зимний месяц')
elif 5 >= months[num_mo-1] > 2:
    print(f'Это весенний месяц')
elif 8 >= months[num_mo-1] > 5:
    print(f'Это летний месяц')
elif 11 >= months[num_mo-1] > 8:
    print(f'Это осенний месяц')
