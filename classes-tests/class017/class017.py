""""
In-class activity demonstrating the concept of operator overloading in Python using the magic methods.
"""

class Wallet:

    def __init__(self, value:int|float=0):
        self.__balance = value

    def __str__(self) -> str:
        return f'You have ${self.__balance:.2f} in your wallet.'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        raise PermissionError('You do not have authorization to change the balance.')

    def __eq__(self, other:object):
        if self.__balance == other.__balance:
            return True
        else:
            return False

    def __iadd__(self, value:int|float):
        self.__balance = self.__balance + value
        return self

    def __isub__(self, value:int|float):
        self.__balance = self.__balance - value
        return self

    def __lt__(self, other):
        if self.__balance <= other.__balance:
            return True
        else:
            return False
