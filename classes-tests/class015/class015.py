"""
An in-class activity designed to demonstrate the behavior of polymorphism in Python through code—specifically, the overriding of methods from a super class.
"""

class Mother:
    def __init__(self, name:str='mom'):
        self.name = name


    def make_cake(self):
        print(f'{self.name} makes CARROT CAKE with sour cream frosting.')

    def fry_chicken(self):
        print(f'{self.name} fries CHICKEN in soybean oil.')



class Daughter(Mother):
    def make_cake(self): #override mother's method
        print(f'{self.name} makes CHOCOLATE CAKE with strawberry jam frosting.')


class Son(Mother): #override mother's method
    def fry_chicken(self):
        print(f'{self.name} fries chicken in the air fryer.')

