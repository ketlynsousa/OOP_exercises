from rich import print

class BankAccount:
    """
    Creates a bank account and allows withdrawals and deposits.
    This bank account requires an 'ID' and name as mandatory fields, and the balance is optional.
    This class has methods for depositing and withdrawing funds from the bank account.
    """
    def __init__(self, id, name, balance=0): # Constructor Method
        self.id = id # public(+)
        self._holder = name # protected (#)
        self.__balance = balance # private (-)

        print(f'Account {self.id} was [bold green]successfully created[/]. Current balance: ${self.__balance:,.2f}')

    def __str__(self): # Dunder Attribute
        #return  f'The account {self.id} for {self._holder} has ${self.__balance:,.2f} of balance.'
        return f'Current Account Statement: {self.__dict__}'

    def deposit(self, value):
        value = abs(value)
        self.__balance += value
        print(f'- Deposit of ${value:,.2f} authorized on the account {self.id}.')

    def withdrawal(self, value):
        value = abs(value)
        if value > self.__balance:
            print(f'Withdrawal denied of ${value:,.2f} on the account {self.id}. INSUFFICIENT BALANCE.')
        else:
            self.__balance -= value
            print(f'- Withdrawal of ${value:,.2f} authorized on the account {self.id}.')
