from animal import Animal


class Dog(Animal):
    def __init__(self, name, specie, age, function):
        super().__init__(name, specie, age)
        self.function = function


    def __str__(self) -> str:
        return f'Animal: {self.specie} | Name: {self.name} | Age: {self.age} | Function: {self.function}'
