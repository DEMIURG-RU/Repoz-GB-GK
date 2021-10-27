from random import randint

with open('task_f.txt', mode='w+', encoding='utf-8') as t_f:
    t_f.write(' '.join([str(randint(1, 1000)) for _ in range(10000)]))
    t_f.seek(0)
    print(sum(map(int, t_f.readline().split())))
