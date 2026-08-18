from classes import *


def main():
    e1 = Student('José', 17, 'IT', 'T01')
    e1.birthday()
    e1.college_enrollment()
    e1.studies()

    p1 = Professor('Manuel', 37, 'Biology', 'Master')
    p1.give_classes()
    p1.studies()

    e1 = Employee('Claudia', 27, 'Secretary', 'Administration')
    e1.clock_in()
    e1.birthday()
    e1.studies()


if __name__ == '__main__':
    main()