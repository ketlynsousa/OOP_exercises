# Implement an object-oriented thermostat. Limited to a minimum 16°C degrees and maximum 30°C.
# When you turn it on, the thermostat starts at 24°C.
# And as you turn it to increase or decrease the temperature, it changes by 0.5°C.
"""
 - Thermostat (class)
 - __temperature
 - @temperature # validate temperature attribute
 - @ftemperature # return formatted temperature
"""


class Thermostat:
    def __init__(self):
        self.__temperature = 24

    @property
    def temperature(self): #Getter
        return self.__temperature

    @temperature.setter
    def temperature(self, value): #Setter
        if not (value * 2).is_integer():
            raise ValueError(f'Temperature of {value}{chr(176)}C is invalid!')
        if value < 16:
            self.__temperature = 16
        elif value > 30:
            self.__temperature = 30
        else:
            self.__temperature = value

    @property
    def ftemperature(self): # Formatted Getter
        return f'{self.__temperature}{chr(176)}C'
