import re

class DataAs:
    def __init__(self, data):
        self.data = data
        self.val_data(data)

    @staticmethod
    def val_data(d):
        if bool(re.match('^[0-9-]*$', d)):
            print(d)
            print(f'Вы ввели коректную дату.')
        else:
            return print('Вы ошиблись с вводом даты.')

    @classmethod
    def tran_ch(cls, data):
        day, month, year = map(int, data.split('-'))
        print(f'Теперь введенная вами строка даты, представлена цыфрами: {day}-{month}-{year}')

in_data = DataAs('20-12-2021')
date2 = DataAs.tran_ch('20-12-2021')








