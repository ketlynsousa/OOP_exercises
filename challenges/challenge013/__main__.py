from challenges.challenge013.thermostat import Thermostat
from rich import print

def main():
    t = Thermostat()
    try:
        t.temperature = 22.3
    except Exception as e:
        print(f'Error: {e}')

    print(f' - Current temperature is {t.ftemperature}')

if __name__ == '__main__':
    main()
