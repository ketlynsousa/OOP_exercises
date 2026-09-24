""""
In-class activity to explain the concept of polymorphism using duck typing method in Python.
"""


class Door:
    def open(self):
        print('- Turn the doorknob and push/pull the door.')


class Enterprise:
    def open(self):
        print('- Go to the Entrepreneur Portal with all the documentation to open a CRN.')


class Egg:
    def open(self):
        print('- Crack the shell with a fork and separate the parts over a frying pan.')

class Stone:
    pass

# PYTHONIC POLYMORPHIC DUCK TYPING METHOD
def try_open(obj):
    try:
        obj.open()
    except:
        print(f'Found an error when trying to open an object type {obj.__class__.__name__}')
