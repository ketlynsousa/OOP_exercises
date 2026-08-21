# Simulate the battle system between RPG characters.
# Character (abstract class)
     # - Name  (attribute)
     # - Life (attribute)
     # - Strikes (attribute)
     # - Attack(target, strength) (concrete method)
     # - Receive Damage (damage) (concrete method)
     # - Heal (abstract method)
""" Warrior (subclass)
    - Name (attribute)
    - Life (attribute)
    - Heal (abstract method) """
""" Mage (subclass)
    - Name (attribute)
    - Life (attribute)
    - Heal (abstract method) """

from random import randint, choice
from abc import ABC, abstractmethod
from rich import print


class Character(ABC):
    def __init__(self, name, life):
        self.name = name
        self.life = life
        self.strikes = []
        self.max_life = life

    def attack(self, target, strength):
        if self.life > 0 and target.life > 0:
            chosen_attack = choice(self.strikes)
            print(f'{self.name}({self.life}) attacked {target.name} with [bold yellow]{chosen_attack}[/] of {strength} strength.')
            target.receive_damage(strength)
        else:
            print(f'{self.name} cannot attack {target.name} -> Target or Attacker is dead.')

    def receive_damage(self, damage):
        factor = randint(0, damage)
        self.life -= factor
        if self.life <= 0:
            self.life = 0
            print(f'[red]Game Over! {self.name} is dead![/]')
        else:
            print(f' - {self.name} received {factor} of damage.')

    @abstractmethod
    def heal(self):
        pass


class Warrior(Character):
    def __init__(self, name, life):
        super().__init__(name, life)
        self.strikes = ['Punch', 'Axel Attack', 'Sword Slashing', 'Mighty Jump']

    def heal(self):
        if self.life <= 0:
            print(f'[bold blue]{self.name}[/] is dead and cannot heal!')
            return

        if self.life < self.max_life:
            life_points = randint(0, 100)
            self.life += life_points
            print(f'The [bold blue]{type(self).__name__}[/] wrapped a bandage around the wounds and recovered [red]{life_points} points of life[/]')
        else:
            print(f'The [bold blue]{type(self).__name__}[/] already has {self.life} max life.')


class Mage(Character):
    def __init__(self, name, life):
        super().__init__(name, life)
        self.strikes = ['Fire Ball', 'Static Magic', 'Lightning Strike', 'Staff Attack']

    def heal(self):
        if self.life <= 0:
            print(f'[bold blue]{self.name}[/] is dead and cannot heal!')
            return

        if self.life < self.max_life:
            life_points = randint(0, 100)
            self.life += life_points
            print(f'The [bold blue]{type(self).__name__}[/] prepared a healing potion and recovered [red]{life_points} points of life[/]')
        else:
            print(f'The [bold blue]{type(self).__name__}[/] already has {self.life} max life.')
