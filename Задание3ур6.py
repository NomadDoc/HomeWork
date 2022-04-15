class Worker:
    name = 'Ivan'
    s_name = 'Ivanov'
    position = 'Director'
    _income = {"wage": 1000, "bonus": 500}
    def __init__(self, name, s_name, position, wage, bonus):
        self.name = name
        self.s_name = s_name
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.s_name
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

person = Position('Иван', 'Иванов', 'директор', 1100000, 300000)
print(f'Характеристика сотрудника: {person.name}, {person.s_name}, {person.position}, {person._income}')
print(f'Итоговая зарплата сотрудника: {person.get_full_name()}\n {person.get_total_income()}')
