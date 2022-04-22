rush_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_t4.txt', 'w', encoding='utf-8') as trn_f:
    with open('text_4.txt', encoding='utf-8') as eng_f:
        trn_f.writelines([line.replace(line.split()[0], rush_dic.get(line.split()[0])) for line in eng_f])
        




