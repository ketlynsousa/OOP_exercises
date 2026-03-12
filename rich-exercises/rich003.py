from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')
tabela.add_column('[purple]Nome[/]', width=10, justify='center', style='red')
tabela.add_column('[purple]Preço[/]', width=10, justify='center', style='green')
tabela.add_row('Lápis', '$1.50')
tabela.add_row('Caderno', '$10.20' )

print(tabela)
