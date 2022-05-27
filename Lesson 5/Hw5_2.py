def word_count(string):
    return(len(string.strip().split(' ')))


lines, letters = 0, 0

for line in open('text_3.txt', 'r', encoding='utf-8'):
    lines += 1
    print(f'В строке', lines, word_count(line), 'слова')

print(f'Всего строк: ', lines)

