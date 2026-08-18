from classes import *
from rich import print

def main():
    bird1 = Bird('Jean', 'Robin Bird', 1, 10.2, 'Seeds')
    bird1.record()
    bird1.meal()

    print()

    horse1 = Horse('Grey', 'Brumby Horse', 3, 'Male', 'Dried Grass')
    horse1.record()
    horse1.birthday()
    horse1.meal()

    print()

    dog1 = Dog('Pete', 'German Shepherd Dog', 2, 'Airport Working Dog', 'Kibble')
    dog1.record()
    dog1.meal()


if __name__ == '__main__':
    main()