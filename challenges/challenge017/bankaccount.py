# Enhance the BankAccount exercise by applying the concept of encapsulation.
"""
 - BankAccount - class
 - _id - protected attribute
 - _holder - protected attribute
 - __balance - private attribute
 - __hash - private attribute
 - @name - validated attribute

 - validade_key(key) - method
 - enter_password() - method
 - withdraw(value, key) - method
 - deposit(value) - method
"""
from hashlib import sha256

from pygments.util import docstring_headline
from rich import print


class BankAccount:
    """
    Represents a secure bank account using Object-Oriented Programming (OOP) encapsulation principles.

    This class manages account details such as ID, holder name, balance, and authentication
    via password hashing. Sensitive attributes are protected or private to ensure data security.

    Attributes:
        _id (int): Protected attribute representing the unique identifier for the bank account.
        _holder (str): Protected attribute storing the name of the account holder.
        __balance (float): Private attribute holding the current financial balance.
        __hash (str): Private attribute storing the SHA-256 hash of the account password.

    Methods:
        enter_password() -> str:
            Static method that interactively prompts the user for a password of at least 6 characters.
        validade_key(key: str) -> bool:
            Validates an input password by comparing its SHA-256 hash with the stored hash.
        deposit(value: float):
            Adds a positive amount to the account balance.
        withdrawal(value: float, key: str = None):
            Deducts an amount from the account balance after verifying the user's password
            and ensuring sufficient funds.
        name (property):
            Getter and setter property for the account holder's name. Updating the name requires
            password authentication and a valid string length.
    """
    def __init__(self, id, holder=None, balance = 0, key=None):
        self._id:int = id
        self._holder:str = holder
        self.__balance:float = balance
        if key is None:
            print(f'Password required to create account...')
            key:str = self.enter_password()
        self.__hash = sha256(str(key).encode('utf-8')).hexdigest()
        print(f'Account {self._id} created successfully. Current balance: ${self.__balance:.2f}')


    @staticmethod
    def enter_password() -> str:
        from pwinput import pwinput
        while True:
            password = str(pwinput('Enter password: ')).strip()
            if len(password) >= 6:
                break
        return password

    def __str__(self) -> str:
        return f'Account: {self._id} | holder: {self._holder} | Balance: ${self.__balance:.2f}'

    def validade_key(self, key:str) -> bool:
        user_password = sha256(key.encode('utf-8')).hexdigest()
        if user_password == self.__hash:
            print(f'[green]Correct password![/]')
            return True
        else:
            print(f'[red]Incorrect password![/]')
            return False

    def deposit(self, value:float):
        value = abs(value)
        self.__balance += value
        print(f'- Deposit of ${value:,.2f} authorized on the account {self._id}.')

    def withdrawal(self, value:float, key=None):
        value = abs(value)

        if key is None:
            print('Password required for withdrawing!')
            key = self.enter_password()

        if self.validade_key(key):
            if value > self.__balance:
                print(f'Withdrawal denied of ${value:,.2f} on the account {self._id}. INSUFFICIENT BALANCE.')
            else:
                self.__balance -= value
                print(f'- Withdrawal of ${value:,.2f} authorized on the account {self._id}.')
        else:
            print('[red]Password does not match. Withdrawal not authorized![/]')


    @property
    def name(self): # Getter
        return self._holder

    @name.setter
    def name(self, newname:str): # Setter
        print(f"Enter password to change holder's name!")
        key = self.enter_password()

        if self.validade_key(key):
            if len(newname) >= 3:
                self._holder = newname
            print("[green]Holder's name changed successfully![/]")

        else:
            print('[red]Password does not match. Name change not successfully![/]')

