from rich import print
from rich.table import Table

global table
table = Table(title="[bold][red]TODAY'S MENU[/]")
table.add_column('Product', width=25, justify='center', style='blue')
table.add_column('Price', width=10, justify='center', style='green')
table.add_row('Spaghetti Bolognese', '$10.50')
table.add_row('Rice With Chicken', '$7.60')
table.add_row('Burger', '$9.50')


def add_item(name, price):
    table.add_row(f'{name}', f'${price:.2f}')

print(table)
add_item('Sausage Roll', 4.50)
add_item('Penne au Gratin', 13.20)
print(table)
