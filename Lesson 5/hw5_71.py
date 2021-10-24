import json
from statistics import mean

with open('mf_71.json', 'w', encoding='utf-8') as wr_f:
    with open('text_7.txt', encoding='utf-8') as fobj:
        prft = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in fobj}
        res = mean(prft.values())
    json.dump(prft, wr_f, ensure_ascii=False, indent=4)
    json.dump(res, wr_f, ensure_ascii=False, indent=4)


