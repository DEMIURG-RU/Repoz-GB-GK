m_lst = list(input("Введите ряд чисел без пробела"))
print(m_lst) # для провеки рокировки
for i in range(1, len(m_lst), 2):
    m_lst[i -1], m_lst[i] = m_lst[i], m_lst[i -1]
print(m_lst)