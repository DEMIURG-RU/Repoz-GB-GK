from abc import ABC, abstractmethod

def abstractmethot(args):
    pass


class Clothes(ABC):
    instances = []

    def __init__(self, param):
        self.param = param
        Clothes.instances.append(self)

    @abstractmethot
    def cloth_consum(self):
        pass

    def __del__(self):
        if self in Clothes.instances:
            Clothes.instances.remove(self)

class Coat(Clothes):
    @property
    def cloth_consum(self):
        return round(self.param / 6.5 + 0.5, 2)

class Suit(Clothes):
    @property
    def cloth_consum(self):
        return round((self.param * 2 + 0.3) / 100, 2)
        
coat1 = Coat(50)
suit1 = Suit(160)
suit2 = Suit(210)

tot_cl_consum = 0
for wear in Clothes.instances:
    tot_cl_consum += wear.cloth_consum
print(f'Общий расход ткани: {tot_cl_consum}')
coat1.__del__()

tot_cl_consum = 0
for wear in Clothes.instances:
    tot_cl_consum += wear.cloth_consum
print(f'Общий расход ткани: {tot_cl_consum}')
coat1.__del__()




