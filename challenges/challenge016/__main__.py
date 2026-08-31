from rich import inspect, print
from challenges.challenge016.rectangle import Rectangle


def main():
    r = Rectangle(4, 8)
    try:
        r.base = 4
        r.height = 12

        r.dimensions = ('tip', 7)
    except Exception as e:
        print(f'[red]Error type = {type(e).__name__}: {e}[/]')

    print(r.dimensions)

    #inspect(r, private=True)

if __name__ == '__main__':
    main()
