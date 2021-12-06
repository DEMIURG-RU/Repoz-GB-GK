def check_wh(vvv, vvvv, vvvvv):
    y = vvv['type']
    for q in y:
        if q == '1':
            mfu_dict[vvvv] += vvvvv
            print(mfu_dict)
        elif q == '2':
            prt_dict[vvvv] += vvvvv
            print(prt_dict)
        else:
            xrx_dict[vvvv] += vvvvv
            print(xrx_dict)

prt_dict = {'2X00': 0, '2X01': 0, '2X10': 0, '2X11': 0, '2C00': 0, '2C01': 0, '2C10': 0, '2C11': 0, '2H00': 0, '2H01': 0, '2H10': 0, '2H11': 0, '2P00': 0, '2P01': 0, '2P10': 0, '2P11': 0}
mfu_dict = {'1X00': 0, '1X01': 0, '1X10': 0, '1X11': 0, '1C00': 0, '1C01': 0, '1C10': 0, '1C11': 0, '1H00': 0, '1H01': 0, '1H10': 0, '1H11': 0, '1P00': 0, '1P01': 0, '1P10': 0, '1P11': 0}
xrx_dict = {'3X00': 0, '3X01': 0, '3X10': 0, '3X11': 0, '3C00': 0, '3C01': 0, '3C10': 0, '3C11': 0, '3H00': 0, '3H01': 0, '3H10': 0, '3H11': 0, '3P00': 0, '3P01': 0, '3P10': 0, '3P11': 0}
prt_key = ''.join(list(dict.keys(prt_dict)))
mfu_key = ''.join(list(dict.keys(mfu_dict)))
xrx_key = ''.join(list(dict.keys(xrx_dict)))
mn_keys = mfu_key + prt_key + xrx_key

z = input('Какой тип оборудования вы привезли? Для МФУ введите 1, Принтеры-2, Ксероксы-3: ')
x = input('Какой марки рборудование вы доставили? Ввведите X - Xerox, С - Canon, H - HP, P - Pantum: ')
d = input('Для Ч/Б - 0, Цветной - 1: ')
u = input('Формат А4 - 0, А3+А4 - 1: ')
haw_many = int(input('Какое количество (только цифры): '))
entr_wh = {'type': z, 'name': x, 'color': d, 'frmt': u, 'quant': haw_many}
q = [z, x, d, u]
w = ''.join(q)
b = mn_keys.find(w, 0)
www = {w: haw_many}

if b >= 0:
    check_wh(entr_wh, w, haw_many)
    print(f'На склад поступил товар: ', w, 'В количестве: ', haw_many)
else:
    print('Вы ошиблись с вводом')





