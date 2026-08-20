# Create classes capable of calculating shipping costs for different vehicles.
# Transport(abstract class)
     # - Distance (attribute)
     # - Shipping Fee (attribute)
     # - Shipping Cost Calculation (abstract method) # Use only distance to calculate the fee
""" Motorcycle (subclass)
        - Factor = 0.50 (class attribute)
        - Shipping Cost Calculation (abstract method)
        Motorcycle shipping is free regardless of the distance; there are no minimum or maximum distance limits. """
""" Truck (subclass)
        - Factor = 1.20 (class attribute)
        - Shipping Cost Calculation (abstract method) 
        The minimum distance required for the truck to make a delivery is 50 km; it does not make trips shorter than that. """
""" Drone (subclass)
        -  Factor = 9.50 (class attribute)
        - Shipping Cost Calculation (abstract method) 
        The drone has a limited battery, so it can only make deliveries of up to 10 km. """

from abc import ABC, abstractmethod
from rich import print

class Transport(ABC):
    def __init__(self, distance, shipping_fee):
        self.distance = distance
        self.shipping_fee = shipping_fee

    @abstractmethod
    def shipping_cost(self):
        pass


class Motorcycle(Transport):
    factor = 0.50
    def __init__(self, distance):
        super().__init__(distance, shipping_fee=Motorcycle.factor)

    def shipping_cost(self):
        return f'$[green]{self.shipping_fee * self.distance:.2f}[/]'


class Truck(Transport):
    factor = 1.20
    def __init__(self, distance):
        super().__init__(distance, shipping_fee=Truck.factor)

    def shipping_cost(self):
        if self.distance >= 50:
            return f'$[green]{self.shipping_fee * self.distance:.2f}[/]'
        else:
            return '[red]Minimum delivery radius of 50 km[/]'


class Drone(Transport):
    factor = 9.50
    def __init__(self, distance):
        super().__init__(distance, shipping_fee=Drone.factor)

    def shipping_cost(self):
        if self.distance <= 10:
            return f'$[green]{self.shipping_fee * self.distance:.2f}[/]'
        else:
            return '[red]Maximum delivery radius of 10 km[/]'

