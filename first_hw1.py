name = input("Введите ваше имя: ")
age = int(input("Укажите ваш возраст: "))
height = int(input("Укажите ваш рост в см: "))
weight = int(input("Укажите ваш вес в кг: "))
# Переводим Рост из см в м
height = height/100
# Определяем индекс массы тела - imt
imt = int(weight /(height**2))
print(f'{name} ваш индекс массы тела: {imt}.')
if imt >= 20 and imt <= 25:
    print(f'У вас {name} отличные показатели. Так держать!')
else:
    print('Вам необходимо заняться своим здоровьем.')



