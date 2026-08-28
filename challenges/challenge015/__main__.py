from challenges.challenge015.credential import Credential
from rich import inspect, print


def main():
    c = Credential()

    c.password = str(input('Enter password: '))
    c.validate(str(input('Enter password again: ')))

if __name__ == '__main__':
    main()

