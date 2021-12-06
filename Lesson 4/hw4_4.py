from random import randint

#gen_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] проверка правильности работы
gen_list = [randint(0, 40) for _ in range(8)]
print(gen_list) #для контроля

md_dict = {i: 0 for i in gen_list}
print(md_dict) #для контроля выполнения
for i in gen_list:
    md_dict[i] += 1

print([i for i in md_dict if md_dict[i] == 1])
