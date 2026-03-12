from rich import print
class Alunos:
    def __init__(self, name, * grades):
        self.name = name
        self.grades = [* grades]

    def average(self):
        res = sum(self.grades) / len(self.grades)
        return f'{res:.2f}'

    def message(self):
        print(f'Aluno: [blue]{self.name}[/] | Grades: [green]{self.grades}[/] got the average [green]{self.average()}[/]')


aluno = Alunos('Ketlyn', 4.5, 8.9, 7.9, 6.1, 7.8)
aluno.message()
