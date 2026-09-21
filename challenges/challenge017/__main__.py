from rich import inspect
from challenges.challenge017.bankaccount import BankAccount


def main():
    cc = BankAccount(117, 'Paul', 5000)

    cc.withdrawal(500)

    cc.name = 'Jonas'

    print(cc)




if __name__ == '__main__':
    main()
