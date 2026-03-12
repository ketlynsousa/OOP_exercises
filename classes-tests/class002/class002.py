# Declaração de Classe
class StudentRegister:
    def __init__(self, name='empty', grade1=0.0, grade2=0.0): # Método construtor
        # Atributos de instância
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2

    # Métodos de instância
    def Average(self):
        result = (self.grade1 + self.grade2) / 2
        return f'{result:.2f}'

    def __getstate__(self):
        return f'Student: {self.name.title()} | Grade 1: {self.grade1} | Grade 2: {self.grade2} | Average: {self.Average()}'

# Declaração de Objeto 1
student1 = StudentRegister()
student1.name = str(input('Enter the name: '))
student1.grade1 = float(input('Enter first grade: '))
student1.grade2 = float(input('Enter second grade: '))

print(student1.__getstate__())
print()

# Declaração de Objeto 2
student2 = StudentRegister()
student2.name = str(input('Enter the name: '))
student2.grade1 = float(input('Enter first grade: '))
student2.grade2 = float(input('Enter second grade: '))

print(student2.__getstate__())
