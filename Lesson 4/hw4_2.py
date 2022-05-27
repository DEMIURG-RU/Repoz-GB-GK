from random import randint

spec_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answ_list = [num for i, num in enumerate(spec_list[1:]) if num > spec_list[i]]

print(f'{spec_list}\n{answ_list}')
