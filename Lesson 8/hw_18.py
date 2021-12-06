class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def data_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and month <= 12 and year <= 3999:
            print('Вы ввели корректную дату')

    @classmethod
    def fr_str(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        print(f'Теперь введенная дата состоить из цыфр: {day}-{month}-{year}')

data_valid = Date.data_valid('20-12-2021')
date2 = Date.fr_str('20-12-2021')