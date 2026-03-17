from rich import print
from rich.table import Table

table = Table(title='Price Table')
table.add_column('[purple]Name[/]', width=10, justify='center', style='red')
table.add_column('[purple]Price[/]', width=10, justify='center', style='green')
table.add_row('Pencil', '$1.50')
table.add_row('Notebook', '$10.20' )

print(table)
