class Animal:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def birthday(self):
        self.age += 1
        print(f'Happy {self.age}th birthday, {self.name}!')
