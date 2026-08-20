from transports import *
from rich.table import Table
from rich import print


def main():
    dist = 20
    delivery = Motorcycle(dist)
    print(f' - Delivering fee of {type(delivery).__name__} for {dist}Km = {delivery.shipping_cost()}')
    print()

    dist = 80
    delivery = Truck(dist)
    print(f' - Delevering fee of {type(delivery).__name__} for {dist}Km = {delivery.shipping_cost()}')
    print()

    dist = 8
    delivery = Drone(dist)
    print(f' - Delivering fee of {type(delivery).__name__} for {dist}Km = {delivery.shipping_cost()}')
    print()


    distance = 70
    travels = [Motorcycle(distance), Truck(distance), Drone(distance)]
    table = Table(title="[bold][italic]Delivery Fee Table[/]")
    table.add_column('Distance', width=20, justify='center', style='blue')
    table.add_column('Type', width=20, justify='center', style='blue')
    table.add_column('Fee', width=40, justify='center')
    for item in travels:
        table.add_row(f'{distance}Km', f'{type(item).__name__}', f'{item.shipping_cost()}')

    print(table)

if __name__ == '__main__':
    main()
