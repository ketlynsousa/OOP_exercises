# Declaração de Classe
class Dogs:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.name = ''
        self.breed = ''
        self.age = 0
        self.adopted = False
    # Métodos de instância
    def birthday(self):
        self.age += 1

    def message(self):
        return f'Dog: {self.name} | Breed: {self.breed} | Age: {self.age} | Adoption Status: {self.adopted}'

# Declaração Objeto 1
dog1 = Dogs()
dog1.name = str(input('Enter name: ')).title().strip()
dog1.breed = str(input('Enter breed: ')).title().strip()
dog1.age = int(input('Enter the age: '))
dog1.adopted = True
print(dog1.message())
print()
# Declaração de Objeto 2
dog2 = Dogs()
dog2.name = str(input('Enter name: ')).title().strip()
dog2.breed = str(input('Enter breed: ')).title().strip()
dog2.age = int(input('Enter the age: '))
dog2.birthday()
print(dog2.message())
