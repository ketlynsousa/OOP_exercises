# Implement the following structure using aggregation, including overloading the + operator to add products to the shopping cart.


"""" - Cart [class]
     - +products = []
     - +@total """

""" - Product [class]
    - +name
    - +price  """


class Product:
    """
        Represents an item available for purchase.

        Attributes:
            name (str): Public attribute storing the product name.
            price (int | float): Public attribute storing the price of the product.
        """

    def __init__(self, name:str = '', price:int|float = 0.0):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} ({currency_formatting(self.price)})'



class Cart:
    """
        Represents a shopping cart containing an aggregated list of products.

        Attributes:
            products (list[Product]): Public attribute storing a list of `Product` instances.

        Properties:
            total (float | int): Read-only property that calculates the sum of all product
                prices in the cart.

        Special Methods:
            __add__(other): Overloads the `+` operator to allow adding a `Product` or
                combining another `Cart` instance, returning a new `Cart`.
        """

    def __init__(self, products:list = None):
        self.products = products if products else []

    @property
    def total(self):
        return sum(item.price for item in self.products)

    def __add__(self, other):

        if isinstance(other, Product):
            return Cart(self.products + [other])

        elif isinstance(other, Cart):
            return Cart(self.products + other.products)

        else:
            raise TypeError('You tried to add an invalid product to the Cart.')

    def __str__(self) -> str:
        items = '\n* '.join(str(p) for p in self.products)
        return f'\n* {items}\n' + '-' * 30 + f'\nTotal: {currency_formatting(self.total)}'


def currency_formatting(value:float|int):
    """
        Formats a numeric value into a US currency string ($).

        Args:
            value (float | int): The numerical amount to be formatted.

        Returns:
            str: The currency-formatted string (e.g., "$10.00").
        """

    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.currency(value, grouping=True)

