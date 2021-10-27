import re

sth = {}

with open('text_6.txt') as fut:
    for line in fut.readlines():
        sth[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
        print(sth)
        