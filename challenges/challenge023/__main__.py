from challenges.challenge023.cart import *

def main():

    p1 = Product('Laptop', 8_500)
    p2 = Product('Mouse', 250)
    p3 = Product('Headset', 450.35)

    # print(p1)
    # print(p2)
    # print(p3)

    c1 = Cart()
    c1 += p1
    c1 += p2
    c1 += p3

    c2 = Cart()
    c2 = c2 + c1

    print(c1)
    print(c2)


if __name__ == '__main__':
    main()
