name = input("Введите ваше имя: ")
age = int(input("Укажите ваш возраст: "))
height = int(input("Укажите ваш рост в см: "))
weight = int(input("Укажите ваш вес в кг: "))
# Переводим Рост из см в м
height = height/100
# Определяем индекс массы тела - imt
imt = int(weight /(height**2))
print(name, 'ваш индекс массы тела: ', imt)




