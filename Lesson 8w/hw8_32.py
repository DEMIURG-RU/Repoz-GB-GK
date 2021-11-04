class MyErrNoInt(Exception):
    def __init__(self, text):
        self.text = text

def chec_inp_num():

    while True:
        in_list = input('Введите число или строку из чисел. Для окончания ввода введите "stop":  ')

        if in_list == "stop":
             return print('Вы закончили ввод')
        else:
             try:
                 if str.isdigit(in_list):
                     s = str(in_list)
                     print('Вы ввели число: ', s, end = " ")
                     print(f' ')
                 else:
                      raise MyErrNoInt('Вы ввели кроме чисел - СИМВОЛ!!')
             except (TypeError, MyErrNoInt) as err:
                 return print(err)

chec_inp_num()
