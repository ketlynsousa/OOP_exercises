class Assessment:
    def __init__(self, name, subject, grade=0):
        self.name = name
        self.subject = subject
        self._grade = grade # protected Attribute (#)

    # Validatable attributes
    @property
    def grade(self): # Getter
        return self._grade

    @grade.setter
    def grade(self, value): # Setter
        if 0 <= value <= 10:
            self._grade = value
        else:
            print('Invalid grade!')
