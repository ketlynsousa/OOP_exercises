from challenges.challenge018.person import Student

def main():
    student1 = Student('Ana', 2000, 'ADM')
    student1.birth = 2002
    print(f'Student1 age: {student1.age}')

    student2 = Student('Marcus', 2006, 'Software Engineer')
    print(f'Student2 age: {student2.age}')

    student3 = Student('Mike', 2008, 'IT')
    print(f'Student3 age: {student3.age}')

    print()
    print(f'OFFICIAL COURSE LIST:')
    print(student1.official_courses)

    print()
    student1.course = 'Marketing'
    student3.course = 'Game Design'
    student3.add_course('Game Design')
    student3.course = 'Game Design'

if __name__ == '__main__':
    main()
