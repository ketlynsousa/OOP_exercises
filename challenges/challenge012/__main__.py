from character import *

def main():
    cha= Warrior('Kratos', 2000)
    cha1 = Mage('Merlin', 3000)

    cha.attack(cha1, 500)
    cha1.attack(cha, 800)
    cha.attack(cha1, 500)
    cha1.attack(cha, 800)
    cha.heal()
    cha.attack(cha1, 1000)
    cha1.heal()
    cha1.attack(cha, 1000)
    cha.attack(cha1, 800)
    cha1.attack(cha, 600)
    cha.heal()

if __name__ == '__main__':
    main()
