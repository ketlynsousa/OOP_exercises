from rich import inspect
from student import Student
from professor import Professor
from employee import Employee


def main():
    a1 = Student('José', 17, 'IT', 'T01')
    a1.grow_old()
    a1.college_enrollment()
    #inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biology', 'Master')
    p1.give_classes()
    #inspect(p1, methods=True)

    e1 = Employee('Claudia', 27, 'Secretary', 'Administration')
    e1.clock_in()
    e1.grow_old()
    #inspect(e1, methods=True)

if __name__ == '__main__':
    main()
