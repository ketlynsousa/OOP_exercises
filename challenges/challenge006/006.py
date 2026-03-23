# Create a class called Pen that simulates the operation of a colored pen, allowing it to write in the relative color.

from rich import print

class Pen:
    def __init__(self, color='white'):
        self.color = color.lower().strip()
        self.capped = True

    def uncap(self):
        self.capped = False

    def cap(self):
        self.capped = True

    def write(self, txt):
        if self.capped:
            print(f':prohibited:[red]The pen [{self.color}]{self.color}[/] is capped. Cannot write.[/]')
        else:
            print(f'[{self.color}] {txt} [/]')

    @staticmethod
    def break_line(qtt=1):
        return print('\n' * qtt)

# Main program
p1 = Pen("Blue")
p2 = Pen("red")
p3 = Pen("Green")

p1.uncap()
p2.uncap()
p3.uncap()

p1.write('Hello! How are you ?')
p1.break_line(2)
p2.write('Hello Gafanhoto! Lets do classes-tests.')
p3.write('Learning Python with Curso em Video')
p3.break_line(1)
p3.cap()
p3.write('Is it going to work with capped pen ?')
