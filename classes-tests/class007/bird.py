from animal import Animal


class Bird(Animal):
    def __init__(self, name, specie, age, size):
        super().__init__(name, specie, age)
        self.size = size


    def __str__(self) -> str:
        return f'Animal: {self.specie} | Name: {self.name} | Age: {self.age} | Size: {self.size}'
