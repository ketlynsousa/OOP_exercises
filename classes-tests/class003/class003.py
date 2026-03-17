class BankAccount:
    """
    Creates a bank account and allows withdrawals and deposits.
    This bank account requires an 'ID' and name as mandatory fields, and the balance is optional.
    This class has methods for depositing and withdrawing funds from the bank account.
    """

    def __init__(self, id, name, balance=0): # Constructor Method
        # Atributos de Instância
        self.id = id
        self.holder = name
        self.balance = balance

    # Métodos de Instância
    def __str__(self): # Dunder Attribute
        return  f'The account {self.id} for {self.holder} has ${self.balance:,.2f} of balance.'

    def deposit(self, value):
        self.balance += value
        print(f'- Deposit of ${value:,.2f} authorized on the account {self.id}.\n')

    def withdrawal(self, value):
        if value > self.balance:
            print(f'Withdrawal denied of ${value:,.2f} on the account {self.id}.\nINSUFFICIENT BALANCE.')
        else:
            self.balance -= value
            print(f'- Withdrawal of ${value:,.2f} authorized on the account {self.id}.')


# Main Program
account1 = BankAccount(112, 'Gustavo', 3000)
account1.deposit(500)
account1.withdrawal(2_000_000)
print(account1)
