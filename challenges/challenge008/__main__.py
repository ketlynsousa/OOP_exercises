from challenges.challenge008.polygon import Square, Circle
from rich import print

def main():
    p1 = Square(12)
    print(f'Perimeter: [blue]{p1.perimeter():.1f}[/]')
    print(f'Area: [blue]{p1.area():.1f}[/]')

    print()

    p2 = Circle(20)
    print(f'Perimeter: [blue]{p2.perimeter():.1f}[/]')
    print(f'Area: [blue]{p2.area():.1f}[/]')

if __name__ == '__main__':
    main()
