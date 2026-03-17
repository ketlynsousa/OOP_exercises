from rich import print
class Student:
    def __init__(self, name, * grades):
        self.name = name
        self.grades = [* grades]

    def average(self):
        result = sum(self.grades) / len(self.grades)
        return f'{result:.2f}'

    def message(self):
        print(f'Student: [blue]{self.name}[/] | Grades: [green]{self.grades}[/] got the average [green]{self.average()}[/]')


student1 = Student('Ketlyn', 4.5, 8.9, 7.9, 6.1, 7.8)
student1.message()
