class Person:
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age

    def grow_old(self):
        self.age += 1
