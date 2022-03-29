my_str = 'Мне нравяться сложные и интересные головоломки'
my_rstr = my_str.split()
ch_el = len(my_rstr)
for t in range(0, ch_el):
    ch_w = len(my_rstr[t])
    if ch_w <= 10:
        print(f'{t+1} {my_rstr[t]}')
    else:
        b = my_rstr[t]
        print(f'{t+1} {b[0:10]}')

