from random import randint

enter_list = [randint(0, 1000) for _ in range(0, randint(2, 100))]
answ_list = [num for i, num in enumerate(enter_list[1:]) if num > enter_list[i]]

print(f'{enter_list}\n{answ_list}')
