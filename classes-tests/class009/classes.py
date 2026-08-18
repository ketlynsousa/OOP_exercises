from rich import print
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def birthday(self):
        self.age += 1
        print(f'Happy {self.age}th birthday, [blue]{self.name}[/]!')

    @abstractmethod
    def meal(self):
        pass


class Bird(Animal):
    def __init__(self, name, specie, age, size, food):
        super().__init__(name, specie, age)
        self.size = size
        self.food = food

    def record(self):
        print(f'Animal: [blue]{self.specie}[/] | Name: [blue]{self.name}[/] | Age: [blue]{self.age}[/] | Size: [blue]{self.size}[/]')

    def meal(self):
        print(f'Animal: {self.specie} is going to eat {self.food} ')


class Horse(Animal):
    def __init__(self, name, specie, age, gender, food):
        super().__init__(name, specie, age)
        self.gender = gender
        self.food = food

    def record(self):
        print(f'Animal: [blue]{self.specie}[/] | Name: [blue]{self.name}[/] | Age: [blue]{self.age}[/] | Gender: [blue]{self.gender}[/]')

    def meal(self):
        print(f'Animal: {self.specie} is going to eat {self.food}.')


class Dog(Animal):
    def __init__(self, name, specie, age, function, food):
        super().__init__(name, specie, age)
        self.function = function
        self.food = food

    def record(self):
        print(f'Animal: [blue]{self.specie}[/] | Name: [blue]{self.name}[/] | Age: [blue]{self.age}[/] | Function: [blue]{self.function}[/]')


    def meal(self):
        print(f'Animal: {self.specie} is going to eat {self.food}.')