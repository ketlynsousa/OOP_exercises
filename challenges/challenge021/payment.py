# Create a simulator that manages payments of different types.
""" - Payment [abstract class]
    - #value [protected attribute]
    - @fvalue [validated attribute]

    - pay() [abstract method] """
""" - Cash [subclass] 
    - pay() [abstract method] """

""" - BankTransfer [subclass]
    - pay() [abstract method] """

""" - CreditCard [subclass] 
    - pay() [abstract method] """

from abc import ABC, abstractmethod
import locale


class Payment(ABC):
    """
        Abstract base class representing a generic payment operation.

        Manages payment amount validation and currency formatting.

        Attributes:
            _value (float): Protected attribute storing the numerical payment amount.

        Properties:
            value (float): Getter/Setter for the payment value. Validates that the amount is strictly positive.
            fvalue (str): Read-only property returning the payment value formatted as US currency ($).

        Methods:
            pay(amount: float): Abstract method that must be implemented by subclasses to process the payment.
        """

    def __init__(self):
        self._value = None

    @abstractmethod
    def pay(self, amount:float):
        pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, amount):
        if amount > 0:
            self._value = amount
        else:
            raise ValueError('The payment can only be done for positive values.')

    @property
    def fvalue(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return locale.currency(self.value, grouping=True)


class Cash(Payment):
    """
        Represents a cash payment method, inheriting base payment properties from Payment.

        Methods:
            pay(amount: float) -> str:
                Processes a cash payment for the given amount and returns a status message.
        """

    def pay(self, amount:float):
        try:
            self.value = amount
            return f'Payment CONFIRMED of {self.fvalue} by Cash.'

        except Exception:
            return f'Payment failure for {self.fvalue} by Cash.'


class BankTransfer(Payment):
    """
        Represents a bank transfer payment method, inheriting base payment properties from Payment.

        Methods:
            pay(amount: float) -> str:
                Processes a bank transfer payment for the given amount and returns a status message.
        """

    def pay(self, amount:float):
        try:
            self.value = amount
            return f'Payment CONFIRMED of {self.fvalue} by Bank Transfer.'

        except Exception:
            return f'Payment failure for {self.fvalue} by Bank Transfer.'


class CreditCard(Payment):
    """
        Represents a credit card payment method, inheriting base payment properties from Payment.

        Methods:
            pay(amount: float) -> str:
                Processes a credit card payment for the given amount and returns a status message.
        """

    def pay(self, amount:float):
        try:
            self.value = amount
            return f'Payment CONFIRMED of {self.fvalue} by Credit Card.'
        except Exception:
            return f'Payment failure for {self.fvalue} by Credit Card.'


def finish_purchase(pay_method:Payment, amount:float):
    """
        Executes a transaction using polymorphic payment methods.

        Args:
            pay_method (Payment): An instance of a subclass of Payment (e.g., Cash, BankTransfer, CreditCard).
            amount (float): The transaction amount to be paid.
        """

    print(pay_method.pay(amount))

