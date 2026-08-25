class Assessment:
    def __init__(self, name, subject, grade=0):
        self.name = name
        self.subject = subject
        self._grade = grade # protected attribute (#)

    # Accessor methods
    def get_grade(self): # Getter Method
        return self._grade

    def set_grade(self, value): # Setter Method
        if 0 <= value <= 10:
            self._grade = value
        else:
            print('Invalid grade!')
