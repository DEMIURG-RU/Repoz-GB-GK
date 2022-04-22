with open('text_3.txt', 'r', encoding='utf-8') as w_p:
    w_d = {line.split()[0]: float(line.split()[1]) for line in w_p}
    print(w_d)
    print(f'Средняя зарплата = {round(sum(w_d.values()) / len(w_d), 3)}\n'
          f'Работники с зарплатой меньше 20К {[e[0] for e in w_d.items() if e[1] < 20000]}')
