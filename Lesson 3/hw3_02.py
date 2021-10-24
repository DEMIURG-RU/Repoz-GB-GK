def m_f(**kwargs):
    print(f'Ваше имя: {name}, Фамилия: {s_name}, Вы родились: {date_b},  Проживаете в: {city_l}, Ваш e-mail: {e_m}, '
          f'Ваш телефон: +7 {phone_m}')
    return

print(f'Введите ваши регистрационные данные')
name = input('Ваше имя: ').capitalize()
s_name = input('Ваша фамилия: ').capitalize()
date_b = input('Дата рождения (чч.мм.гг): ')
city_l = input('Город проживания: ').capitalize()
e_m = input('Ваш e-mail: ')
phone_m = input('Номер телефона: +7 ')
m_f()
