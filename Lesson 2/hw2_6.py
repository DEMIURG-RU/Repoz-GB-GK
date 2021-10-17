product = []
prc_sv = {'Название': '', 'Цена': '', 'Количество': '', 'ЕдИзм': ''}
anltc = {'Название': [], 'Цена': [], 'Количество': [], 'ЕдИзм': []}
num = 0
while True:
    if input('Если вы закончили ввод товара - нажмите "Q", для продолжения ввода нажмите "Enter": ').upper() == 'Q':
        break
    num += 1
    made_copy = prc_sv.copy()
    for t in prc_sv:
        pro_ty = input(f'Введите свойство товара "{t}": ')
        made_copy[t] = int(pro_ty) if t == 'Цена' or t == 'Количество' \
            else pro_ty
        anltc[t].append(made_copy[t])
    product.append((num, made_copy))
    print(f'\nОписание и данные по товару\n{product}')
    print(f'\n Текущая аналитика по товарам: \n {"-" * 30}')
    for key, value in anltc.items():
        print(f'{key:>30}: {value}')
    print("-" * 30)
