from animal import Animal


class Horse(Animal):
    def __init__(self, name, specie, age, gender):
        super().__init__(name, specie, age)
        self.gender = gender


    def __str__(self) -> str:
        return f'Animal: {self.specie} | Name: {self.name} | Age: {self.age} | Gender: {self.gender}'
