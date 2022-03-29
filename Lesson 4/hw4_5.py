from functools import reduce

gen_list = [ch for ch in range(100, 1001, 2)]

print(n := reduce(lambda x, y: x * y, [a for a in gen_list]))


