from class011 import Assessment
from rich import print, inspect

def main():
    a = Assessment('Gabriel', 'Mathematics')
    a.set_grade(7.5)
    print(f'{a.name} received a grade of {a.get_grade()} in the {a.subject} subject.')
    inspect(a, private=True)

if __name__ == '__main__':
    main()
