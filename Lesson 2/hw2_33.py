year_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь',
             11: 'Ноябрь', 12: 'Декабрь',}
month_year = int(input('Введите номер месяца года (значение от 1 до 12): '))
zap_ros = year_dict[month_year]
print(f'Вы указали месяц:  {zap_ros}')
if month_year <= 2 or month_year == 12:
    print(f'Это зимний месяц')
elif 5 >= month_year > 2:
    print(f'Это весенний месяц')
elif 8 >= month_year > 5:
    print(f'Это летний месяц')
elif 11 >= month_year > 8:
    print(f'Это осенний месяц')
