# Simulate an object-oriented coffee maker, this special machine will make coffee, tea and milk.
# HotBeverage(abstract class)
     # - Prepare(concrete method)
     # - Boil Water(concrete method)
     # - Blend (abstract method)
     # - Serve (abstract method)
""" Coffee (subclass)
        - Blend (abstract method)
        - Serve (abstract method) """
""" Tea (subclass)
        - Blend (abstract method)
        - Serve (abstract method) """
""" Milk (subclass)
        - Blend (abstract method)
        - Serve (abstract method) """
from abc import ABC, abstractmethod


class HotBeverage(ABC):

    def prepare(self):
        print('--- Starting Preparation ----')
        print(self.boil_water())
        print(self.blend())
        print(self.serve())
        print('--- Ready-to-drink beverage ---')

    @staticmethod
    def boil_water():
       return '1. Boiling water until it reaches 100°C.'

    @abstractmethod
    def blend(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Coffee(HotBeverage):
    def blend(self):
        return f'2. Passing pressurized water through the ground coffee.'

    def serve(self):
        return f'3. Serving in a small cup.'


class Tea(HotBeverage):
    def blend(self):
        return '2. Submerging the herbal sachet in water.'

    def serve(self):
        return '3. Serving in porcelain cup with cinnamon and lemon.'


class Milk(HotBeverage):
    def blend(self):
        return '2. Steaming the milk until it reaches 65°C.'

    def serve(self):
        return '3. Serving in a large mug, already containing coffee.'
