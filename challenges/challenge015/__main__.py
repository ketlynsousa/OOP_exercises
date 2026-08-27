from challenges.challenge015.credential import Credential
from rich import inspect, print


def main():
    c = Credential()
    c.password = str(input('Enter password: '))
    print(c.password)

    c.validate(' Cricket@! ')

if __name__ == '__main__':
    main()
