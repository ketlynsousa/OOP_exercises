from class012 import Assessment
from rich import print, inspect


def main():
    a = Assessment('Peter', 'History')
    a.grade = 5.5
    print(f'{a.name} received a grade of {a.grade} in the {a.subject} subject.')
    inspect(a, private=True)

if __name__ == '__main__':
    main()
