import json

with open('mf_7.json', 'w', encoding='utf-8') as wr_f:
    with open('text_7.txt', encoding='utf-8') as fobj:
        prft = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in fobj}
        res = [prft, {'Средняя прибыль': round(sum([int(i) for i in prft.values() if int(i) > 0]) /
                                                len([int(i) for i in prft.values() if int(i) > 0]))}]
        json.dump(res, wr_f, ensure_ascii=False, indent=4)

