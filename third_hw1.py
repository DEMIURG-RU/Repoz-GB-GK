nk_num = input("Введите любойе число от 1 до 99: ")
# Получаем слогаемые согласно ТЗ - в строковых переменных
num_02 = nk_num + nk_num
num_03 = num_02 + nk_num
print(nk_num, num_02, num_03)
# Переводим (преобразуем) строковые переменные в целые
cp_1 = int(nk_num)
cp_2 = int(num_02)
cp_3 = int(num_03)
# Определяем сумму введенного числа, сформированного согласно задания
cp_0 = cp_1 + cp_2 + cp_3
print(cp_1, '+', cp_2, '+', cp_3, '=', cp_0)
