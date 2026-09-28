from challenges.challenge021.payment import *

def main():

    finish_purchase(Cash(), 2800)
    finish_purchase(BankTransfer(), 11_555)
    finish_purchase(CreditCard(), 757.90)


if __name__ == '__main__':
    main()
