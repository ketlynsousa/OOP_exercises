from challenges.challenge024.validator import *


def main():

    validate_data(Username(), 'guanabara_123')
    validate_data(Email(), 'guanabara_23@fou.c')
    validate_data(Password(), 'Cricket@@12')

if __name__ == '__main__':
    main()
