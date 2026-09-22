"""
An in-class activity designed to demonstrate the behavior of polymorphism in Python through code—specifically, the overriding of methods from a super class.
"""

from abc import ABC


class Animal(ABC):
    def __init__(self, name:str=''):
        self.name = name

    def make_sound(self):
        print(f'{self.name} is {self.__class__.__name__} and is making a sound.')

class Duck(Animal):
    def make_sound(self): #Override superclass(Animal) method
        print(f'{self.name} just quacked. QUACK! QUACK! QUACK!')


class Dog(Animal):
    def make_sound(self): #Override superclass(Animal) method
        print(f'{self.name} just barked. WOOF! WOOF!')

class GermanSpitz(Dog): #Override subclass(Dog) method
    def make_sound(self):
        print(f'{self.name} just barked. arf!arf!arf!arf!arf!arf!')

class Pitbull(Dog): #Override subclass(Dog) method
    def make_sound(self):
        print(f'{self.name} just barked. RUF! RUF!')

class Cat(Animal): # Override superclass(Animal) method
    def make_sound(self):
        print(f'{self.name} just meowed. MEEOOOW!!')


class Chicken(Animal): # Override superclass(Animal) method
    def make_sound(self):
        print(f'{self.name} just clucked. CLUCK! CLUCK!')
