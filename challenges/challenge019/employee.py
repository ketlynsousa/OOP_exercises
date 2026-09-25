# Create the following class structure to calculate salary bonuses.
""" - Employee [abstract class]
    - +name [public attribute]
    - -salary [private attribute]

    - +calculate_bonus() [abstract method]"""
""" - Manager [subclass]
    - calculate_bonus() #15% bonus """

""" - Designer [subclass]
    - calculate_bonus() #8% bonus """

""" - Developer [subclass]
    - calculate_bonus() #10% bonus """

from abc import ABC, abstractmethod

class Employee(ABC):
    """
        Abstract base class representing a generic employee.

        Serves as the foundation for specific roles, handling public identity,
        private salary management with validation, and enforcing bonus calculation rules.

        Attributes:
            name (str): Public attribute storing the employee's name.
            __salary (float): Private attribute storing the base salary amount.

        Properties:
            salary (float): Getter/Setter for the salary. The setter ensures
                the salary cannot be set to None or reduced below its current value.

        Methods:
            calculate_bonus(): Abstract method that must be implemented by subclasses
                to calculate the specific bonus amount.
        """

    def __init__(self, name:str = None, salary:float= 1621):
        self.name = name
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount:float = None):
        if amount is None:
            raise ValueError("It's impossible to adjust the salary this way.")
        else:
            if amount >= self.__salary:
              self.__salary = amount
            else:
                raise ValueError("You cannot decrease an employee's salary.")

    @abstractmethod
    def calculate_bonus(self):
        pass


class Manager(Employee):
    """
        Represents a manager eligible for a 15% salary bonus.

        Inherits base attributes and salary rules from Employee.

        Attributes:
            bonus (int): Class attribute defining the manager bonus percentage (15%).

        Methods:
            calculate_bonus() -> str:
                Calculates and returns a 15% bonus formatted as currency.
        """

    bonus = 15
    def __init__(self, name:str, salary:float):
        super().__init__(name, salary)

    def calculate_bonus(self):
        bonus = (Manager.bonus / 100) * self.salary
        return f'${bonus:,.2f}'

    def __str__(self) -> str:
        return f'{self.name} earns ${self.salary:,.2f} and for being {self.__class__.__name__} the bonus will be {Manager.bonus}% which it is {self.calculate_bonus()}'


class Designer(Employee):
    """
        Represents a designer eligible for an 8% salary bonus.

        Inherits base attributes and salary rules from Employee.

        Attributes:
            bonus (int): Class attribute defining the designer bonus percentage (8%).

        Methods:
            calculate_bonus() -> str:
                Calculates and returns an 8% bonus formatted as currency.
        """

    bonus = 8
    def __init__(self, name:str, salary:float):
        super().__init__(name, salary)

    def calculate_bonus(self):
        bonus = (Designer.bonus / 100) * self.salary
        return f'${bonus:,.2f}'

    def __str__(self) -> str:
        return f'{self.name} earns ${self.salary:,.2f} and for being {self.__class__.__name__} the bonus will be {Designer.bonus}% which it is {self.calculate_bonus()}'


class Developer(Employee):
    """
        Represents a developer eligible for a 10% salary bonus.

        Inherits base attributes and salary rules from Employee.

        Attributes:
            bonus (int): Class attribute defining the developer bonus percentage (10%).

        Methods:
            calculate_bonus() -> str:
                Calculates and returns a 10% bonus formatted as currency.
        """

    bonus = 10
    def __init__(self, name:str, salary:float):
        super().__init__(name, salary)

    def calculate_bonus(self):
        bonus = (Developer.bonus / 100) * self.salary
        return f'${bonus:,.2f}'

    def __str__(self) -> str:
        return f'{self.name} earns ${self.salary:,.2f} and for being {self.__class__.__name__} the bonus will be {Developer.bonus}% which it is {self.calculate_bonus()}'

