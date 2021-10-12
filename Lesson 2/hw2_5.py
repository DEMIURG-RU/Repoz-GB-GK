m_lst = [9, 9, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
new_rnt = int(input('Введите новый элемент в рейтинг: '))
t = 0
for n in m_lst:
    if new_rnt <= n:
        t += 1
    else:
        break
m_lst.insert(t, new_rnt)
print(m_lst)
