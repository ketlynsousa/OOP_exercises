from challenges.challenge014.diary import Diary
from rich import inspect, print


def main():
    d = Diary('Cricket')
    d.write('First message')
    d.write('Studying Python')
    d.write('Training Encapsulation')

    try:
        d.read()
    except Exception as e:
        print(f'Error: {e}')

    inspect(d, private=True, methods=True)

if __name__ == '__main__':
    main()
