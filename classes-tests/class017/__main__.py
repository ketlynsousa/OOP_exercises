from class017 import *

def main():
    w1 = Wallet(100)
    w2 = Wallet(200)

    w1 += 50
    w1 -= 10
    print(w1)
    print(w2)

    if w1 == w2:
        print(f'Both wallets have the same balance value.')
    else:
        print('- The wallets have different balance values.')

    if w1 < w2:
        print(f'- Second wallet has more money.')
    else:
        print('- First wallet has more money.')


if __name__ == "__main__":
    main()
