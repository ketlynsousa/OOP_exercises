# Implement the following class diagram structure.
"""
 - Person (abstract class)

 - _name - (protected attribute)
 - _birth - (protected attribute)
 - @age - (validated attribute)

 - Student - (subclass)
 - _official_courses = (protected attribute)
 - _course - (protected attribute)
 - @course - (validated attribute)

 - add_course(course) - method
"""
from datetime import date
from abc import ABC
from rich import print


class Person(ABC):
    """
        Abstract base class representing a person.

        Attributes:
            _name (str): Protected attribute storing the person's name.
            _birth (int): Protected attribute storing the person's birth year.

        Properties:
            birth (int): Gets or sets the birth year. Must be between 1900 and the current year.
            age (int): Read-only property that calculates the person's age based on the birth year.
        """

    def __init__(self, name:str, birth:int):
        self._name = name
        self._birth = None
        self.birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, year):
        if 1900 <= year <= date.today().year:
            self._birth = year
        else:
            raise ValueError(f'Year {year} is invalid!')

    @property
    def age(self):
        return date.today().year - self._birth

    @age.setter
    def age(self, age):
        raise PermissionError('You cannot change the age. Change the year of birth!')


class Student(Person):
    """
        Represents a student, inheriting from the Person base class.

        Attributes:
            official_courses (list[str]): Class attribute containing the list of valid course names.
            _course (str | None): Protected attribute storing the student's enrolled course.

        Properties:
            course (str): Gets or sets the enrolled course. Validates whether the course
                is listed in `official_courses`.

        Methods:
            add_course(title: str):
                Static method that validates and appends a new course title to the `official_courses` list.
        """

    official_courses = ['Software Engineer', 'ADM', 'Marketing', 'IT', 'Data Analyst']
    def __init__(self, name:str, birth:int, course:str):
        super().__init__(name, birth)
        self._course = None
        self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, title:str):
        if title in Student.official_courses:
            self._course = title
            print(f'Course set up to [cyan]{title}![/]')
            print(f'{self.__dict__}')
        else:
            self._course = None
            print(f'[red]{title} is not in the official course list.[/]')

    @staticmethod
    def add_course(title:str):
        title = title.strip().title()
        if len(title) >= 3:
            Student.official_courses.append(title)
            print(f'[cyan]{title}[/] [green]added to official course list successfully![/]')

