from rich import print
from abc import ABC, abstractmethod # Abstract Base Classes


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    @abstractmethod
    def studies(self):
        pass


class Student(Person):
    def __init__(self, name, age, course, class_team):
        super().__init__(name, age)
        self.course = course
        self.team = class_team

    def college_enrollment(self):
        print(f'The student [green]{self.name}[/] just has enrolled to the [blue]{self.course}[/] course.')

    def studies(self):
        print(f'[yellow on black]Student [green]{self.name}[/] is currently studying {self.course}.[/]')


class Professor(Person):
    def __init__(self, name, age, speciality, level):
        super().__init__(name, age)
        self.speciality = speciality
        self.level = level

    def give_classes(self):
        print(f'The {self.level} prof.[green]{self.name}[/] started the [blue]{self.speciality}[/] class.')

    def studies(self):
        print(f'[yellow on black]Prof.[green]{self.name}[/] is specialist in {self.speciality} currently at level {self.level}.[/]')


class Employee(Person):
    def __init__(self, name, age, position, sector):
        super().__init__(name, age)
        self.position = position
        self.sector = sector

    def clock_in(self):
        print(f'Employee [green]{self.name}[/] from [blue]{self.sector}[/] just clocked in.')

    def studies(self):
        print(f'[yellow on black]Employee [green]{self.name}[/] currently specialized in {self.sector} area.[/]')