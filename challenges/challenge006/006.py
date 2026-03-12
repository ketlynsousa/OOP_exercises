# Create a class called Pen that simulates the operation of a colored pen, allowing it to write in the relative color.

from rich import print

class Pen:
    def __init__(self, color):
        self.color = color
        self.capped = True

    def uncap(self):
        self.capped = False

    def write(self, txt):
        if self.capped:
            print(f':stop_sign: [red]The pen [{self.color}]{self.color}[/] is capped. Cannot write.[/]')
        else:
            print(f'[{self.color}] {txt} [/]')

    @staticmethod
    def break_line():
        return print('\n')

# Main program
p1 = Pen("blue")
p2 = Pen("red")
p3 = Pen("green")

p1.uncap()
p2.uncap()
p3.uncap()

p1.write('Hello! How are you ?')
p1.break_line()
p2.write('Hello Gafanhoto! Lets do classes-tests.')
p3.write('Learning Python with Curso em Video')
