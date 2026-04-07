from person import Person


class Student(Person):
    def __init__(self, name, age, course = '', class_team = ''):
        super().__init__(name, age)
        self.course = course
        self.class_team = class_team

    def college_enrollment(self):
        print(f'The student {self.name} just has enrolled to the {self.course} course.')
