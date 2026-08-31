# Create a class that represents a rectangle by its dimensions and area.
"""
 - Rectangle - class
 - _base - protected attribute
 - _height - protected attribute
 - _area - protected attribute

 - @base - validated attribute
 - @height - validated attribute
 - @dimensions - validated attribute
 - @area - validated attribute
"""


class Rectangle:
    def __init__(self, base=1, height=1):
        self._base = None
        self._height = None
        self._area = None

        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError('Base value should be a number.')

        if value > 0:
            self._base = value
        else:
            raise ValueError('Invalid value for the base.')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('Height value should be a number.')

        if value > 0:
            self._height = value
        else:
            raise ValueError('Invalid value for the height.')

    @property
    def area(self):
        area = self._base * self._height
        return area

    @area.setter
    def area(self, value):
        raise PermissionError('The area cannot be configured this way.')

    @property
    def dimensions(self):
        return f'Base = {self.base} \nHeight = {self.height} \nArea: {self.area}'

    @dimensions.setter
    def dimensions(self, measures:tuple):
        if not isinstance(measures, tuple):
            raise TypeError('Measures must be informed through a tuple.')
        if len(measures) != 2:
            raise SyntaxError('Inform a tuple with only 2 numeric values.')

        if isinstance(measures[0], float) or isinstance(measures[0], int):
            self.base = measures[0]
        else:
            raise TypeError('Base value should be a number.')
        if isinstance(measures[1], float) or isinstance(measures[1], int):
            self.height = measures[1]
        else:
            raise TypeError('Height value should be a number.')

        if measures[0] > 0:
            self._base = measures[0]
        else:
            raise ValueError('Invalid value for the base.')
        if measures[1] > 0:
            self._height = measures[1]
        else:
            raise ValueError('Invalid value for the height.')
