""""
In-class activity demonstrating the concept of method overloading in Python using the 'singledispatchmethod' method from the functools library.
"""
from functools import singledispatchmethod


class Analyser:

    @singledispatchmethod
    def analyse(self, value):
        print(f"It wasn't possible analyse the value {value}.")

    @analyse.register
    def _(self, value:int):
        print(f'{value} is an integer number.')

    @analyse.register
    def _(self, value:float):
        print(f'{value} is a decimal number.')

    @analyse.register
    def _(self, value:str):
        print(f'{value} is a string sequence.')

    @analyse.register
    def _(self, value: tuple|list|dict):
        print(f'{value} is a collection of data.')
