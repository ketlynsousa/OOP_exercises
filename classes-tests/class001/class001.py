# Declaração de Classe
class StudentRegister:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.name = ''
        self.grade1 = 0.0
        self.grade2 = 0.0

    # Métodos de instância
    def studentAverage(self):
        result = (self.grade1 + self.grade2) / 2
        return f'{result:.2f}'

    def message(self):
        return f'Student: {self.name} | Grade 1: {self.grade1} | Grade 2: {self.grade2}'

# Declaração de Objeto 1
student1 = StudentRegister()
student1.name = str(input('Enter the name: '))
student1.grade1 = float(input('Enter first grade: '))
student1.grade2 = float(input('Enter second grade: '))

print(f'{student1.message()} | Average: {student1.studentAverage()}')

# Declaração de Objeto 2
student2 = StudentRegister()
student2.name = str(input('Enter the name: '))
student2.grade1 = float(input('Enter first grade: '))
student2.grade2 = float(input('Enter second grade: '))

print(f'{student2.message()} | Average: {student2.studentAverage()}')
