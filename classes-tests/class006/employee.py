from person import Person


class Employee(Person):
    def __init__(self, name, age, position = '', sector = ''):
        super().__init__(name, age)
        self.position = position
        self.sector = sector

    def clock_in(self):
        print(f'Employee {self.name} just clocked in.')
