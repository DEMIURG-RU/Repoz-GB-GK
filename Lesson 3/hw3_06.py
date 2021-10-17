def int_func(word):
    char = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(char) else print('Вы нарушили правило ввода')

word = input('Введите слова маленькими английскими буквами через пробел: ').split()
for ch in word:
    res = int_func(ch)
    if res:
        print(int_func(ch), ' ')
