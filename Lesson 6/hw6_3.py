class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self. position = position
        self._income = {'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

vat_worker = Position('Товкайло', 'Владимир', 'инженер-конструктор', 125000, 25000)
print(vat_worker.get_full_name())
print(vat_worker.position)
print(vat_worker.get_total_income())
