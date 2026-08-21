from class010 import BankAccount
from rich import print

def main():
    ac1 = BankAccount(111, 'Jonas', 5_000)
    ac1.deposit(1000)
    ac1._holder = 'Peter' # Python don't force block a protected attribute but the sign should dismiss of programmer changing due to convention called 'Consenting Adults'.
    ac1.__balance = 0 # Here Python did not change the BankAccount balance attribute, it creates another attribute and adds the value 0
    # Only way of actually accessing the name mangling is adding the whole name of class and attribute to change.
    ac1._BankAccount__balance = 0 # Once again, it does not go with convention 'Consenting Adults'

    print(ac1)

if __name__ == '__main__':
    main()
