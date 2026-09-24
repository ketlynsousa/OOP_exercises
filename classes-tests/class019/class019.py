""""
In-class activity to explain the concept of polymorphism using duck typing method in Python.
"""

class Number:
    def __init__(self, value:int|float=0):
        self.value = value

    def __str__(self) -> str:
        return f'- I have the value {self.value} inside of the Number.'

    def double(self):
        self.value = self.value * 2
        return self


class Text:
    def __init__(self, txt:str=''):
        self.text = txt

    def __str__(self) -> str:
        return f'- I have the text "{self.text}" inside of the Text.'

    def double(self):
        self.text = self.text + " " + self.text
        return self


class List:
    def __init__(self, values:list=None):
        if values is None:
            values = []
        self.lst = values

    def __str__(self) -> str:
        return f'- I have the items {self.lst} inside of the List.'

    def double(self):
        self.lst = self.lst + self.lst
        return self


class Paper:
    def __init__(self):
        self.doubled = False

    def __str__(self) -> str:
        return f'- Is it the paper doubled inside the Paper? {self.doubled}'

    def double(self):
        self.doubled = True


class House:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return f'It is just a house...'


# DUCK TYPING METHOD
def try_double(obj:object):
    try:
        obj.double()
    except:
        print(f'I had difficulties to double {obj.__class__.__name__}')
