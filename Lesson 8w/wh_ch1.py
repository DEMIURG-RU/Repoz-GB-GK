class WareH:
    def __init__(self, code_eq, name_eq, frmt_eq, color_eq, quant_eq):
        self.code_eq = code_eq
        self.name_eq = name_eq
        self.frmt_eq = frmt_eq
        self.color_eq = color_eq
        self.quant_eq = quant_eq

    def __str__(self):
        return f'Прежде чем нажать ввод проверьте данные, которые вы ввели: {self.code_eq} {self.name_eq} {self.frmt_eq} {self.color_eq} {self.quant_eq}'

    def prep_for_verif(self, a, b, c, d, y):
        name_dict = {'X': 'Xerox','C': 'Canon', 'H': 'HP', 'P': 'Pantum'}
        type_dict = {'1': 'МФУ', '2': 'Принтер', '3': 'Ксерокс'}
        color_dict = {'0': 'Ч/Б', '1': 'Цветной'}
        frmt_dict = {'0': 'Формат А4', '1': 'Формат А3 и А4'}
        type_key = ''.join(list(dict.keys(type_dict)))
        name_key = ''.join(list(dict.keys(name_dict)))
        color_key = ''.join(list(dict.keys(color_dict)))
        frmt_key = ''.join(list(dict.keys(frmt_dict)))
        print(a, b, c, d, y)
        if a in type_key:
            if b in name_key:
                if c in color_key:
                    if d in frmt_key:
                        if y > 0:
                            print('Вы введи все правильно.')
                    else:
                        return print('Вы ошиблись с вводом формата оборудования. Проверте и повторите ввод.')
                else:
                    return print('Вы ошиблись с вводом цветности оборудования. Проверте и повторите ввод.')
            else:
                return print('Вы ошиблись с вводом марки оборудования. Проверте и повторите ввод.')
        else:
            return print('Вы ошиблись с вводом типа оборудования. Проверте и повторите ввод.')
#        return type_key, name_key, color_key, frmt_key, y

    def opr_dir(self, a, b, c, d, y):
        if WareH.prep_for_verif(self, a, b, c, d, y) != None:
            return print('Программа остановлена')
#        fg = str(a, b, c, d, y)
        else:
            print(a, b, c, d, y)

        w_s = [a, b, c, d, y]
        print(w_s, type(w_s))


class PrtW(WareH):
    def accep_prnt (self, a, b, c, d, y):
#        p_1 = self.prep_for_verif(('type_key')
#        print(p_1)
        vas = [a, b, c, d, y]
        print(vas)





#class MfuW(WareH):

#class XerW(WareH):



#    def chek_eq(self, a, b , c, d):




#class PrtEq(WareH):
#    def to_teach(self, subj, *pupils):
#        for pupil in pupils:
#            pupil.to_take(subj)

#class MultFunDev(WareH):
#    def to_teach(self, subj, *pupils):
#        for pupil in pupils:
#            pupil.to_take(subj)

#class XerEq(WareH):
#    def to_teach(self, subj, *pupils):
#        for pupil in pupils:
#            pupil.to_take(subj)
#--------------------------------------------------------
#class SmartTech:
#    def __init__(self, *subjects):
#        self.subjects = list(subjects)

#    def my_list(self):
#        return self.subjects

#class PrT(SmartTech):
#    def __init__(self, name, surname):
#        super().__init__(name, surname)
#        self.knowledges = []

#    def to_take(self, subj):
#        self.knowledges.append(subj)

#class Comp(SmartTech):
#    def __init__(self, name, surname):
#        super().__init__(name, surname)
#        self.knowledges = []

#    def to_take(self, subj):
#        self.knowledges.append(subj)

#class Xer(SmartTech):
#    def __init__(self, name, surname):
#        super().__init__(name, surname)
#        self.knowledges = []

#    def to_take(self, subj):
#        self.knowledges.append(subj)

#s = Subject('maths', 'physiscs', 'chemistry')
#t = Teacher('Ivan', 'Ivanov')
#print(t)

#p_1 = Pupil('Petr', 'Petrov')
#p_2 = Pupil('Sergey', 'Sergeev')
#p_3 = Pupil('Vladimir', 'Vladimirov')
#print(f'{p_1}; {p_2}; {p_3}')

#t.to_teach(s, p_1, p_2, p_3)
#print(p_1.knowledges[0].my_list())
s = 1
z = input('Какой тип оборудования вы привезли? Для МФУ введите 1, Принтеры-2, Ксероксы-3: ')
x = input('Какой марки рборудование вы доставили? Ввведите X - Xerox, С - Canon, H - HP, P - Pantum: ')
d = input('Для Ч/Б - 0, Цветной - 1: ')
u = input('Формат А4 - 0, А3+А4 - 1: ')
haw_many = int(input('Какое количество (только цифры): '))


a = WareH.prep_for_verif(s, z, x, d, u, haw_many)
b = WareH.opr_dir(s, z, x, d, u, haw_many)
#c = PrtW.accep_prnt(self, a, b, c, d, y)




