# Create a class 'Employee', where we can register name, sector and position.
# Also create a method that allows the employee to introduce themselves.
from rich import print

class Employee:
    # Atributos de Classe
    company = 'Curso em Video'

    def __init__(self, name='', sector='', position=''): # Método Construtor
        # Atributos de instância
        self.name = name
        self.sector = sector
        self.position = position

    # Métodos de instância
    def introduction(self) -> str:
        return (f':handshake: Hello, I am [blue]{self.name}[/] I am {self.position} '
                f'from the sector of {self.sector} for the company "{self.__class__.company}"')


# Main Program
person1 = Employee('Maria', 'Administration', 'Director')
print(person1.introduction())
print()
person2 = Employee('Pedro', 'IT', 'Programmer')
print(person2.introduction())
