from bird import Bird
from horse import Horse
from dog import Dog

def main():
    bird1 = Bird('Jean', 'Robin Bird', 1, 10.2)
    print(bird1)

    horse1 = Horse('Grey', 'Brumby Horse', 3, 'Male')
    horse1.birthday()
    print(horse1)

    dog1 = Dog('Pete', 'German Shepherd Dog', 2, 'Airport Working Dog')
    print(dog1)


if __name__ == '__main__':
    main()
