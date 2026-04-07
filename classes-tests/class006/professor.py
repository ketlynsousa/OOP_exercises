from person import Person


class Professor(Person):
    def __init__(self, name, age, speciality = '', level = ''):
        super().__init__(name, age)
        self.speciality = speciality
        self.level = level

    def give_classes(self):
        print(f'Prof.{self.name} started the {self.speciality} class.')
