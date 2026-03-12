# Declaração de Classe
class Dogs:
    def __init__(self, name='empty', breed='empty', age=0, adoption=False): # Método construtor
        # Atributos de instância
        self.name = name
        self.breed = breed
        self.age = age
        self.adoption = adoption

    # Métodos de instância
    def birthday(self):
        self.age += 1

    def __getstate__(self):
        return f'Dog: {self.name.title()} | Breed: {self.breed.title()} | Age: {self.age} | Adoption Status: {self.adoption}'

# Declaração Objeto 1
name = str(input('Enter name: '))
breed = str(input('Enter breed: '))
age = int(input('Enter the age: '))
dog1 = Dogs(name=name, breed=breed, age=age, adoption=True)
print(dog1.__getstate__())
print()

# Declaração de Objeto 2
name = str(input('Enter name: '))
breed = str(input('Enter breed: '))
age = int(input('Enter the age: '))
dog2 = Dogs(name=name, breed=breed, age=age)
dog2.birthday()
print(dog2.__getstate__())

