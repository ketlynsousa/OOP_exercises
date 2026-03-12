# Create a class called 'Product' where we can register name and price. Also create a method that display a price tag of the product.
from rich.panel import Panel
from rich import print

class Product:
    def __init__(self, name='', price=0.0):
        self.name = name
        self.price = price

    def tag(self):
        content = f'{self.name.center(30)}'
        content += f'{'-' * 30}'
        price_formatted = f'${self.price:,.2f}'
        content += f'{price_formatted.center(30, ".")}'
        tag = Panel(content, width=34, title='Product')
        print(tag)

# Main Program
p1 = Product('iPhone Pro Max', 3_500.90)
p2 = Product('Laptop Lenovo', 6_500.90)
p1.tag()
p2.tag()
