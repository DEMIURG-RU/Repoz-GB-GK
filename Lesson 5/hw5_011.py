s_b = (input('Введите первую строку: '), input('Введите вторую строку: '), input('Введите третью строку: '))

with open('l44_f.txt', 'w', encoding='utf-8') as me_f:
    for i in s_b:
        me_f.writelines(i + '\n')




