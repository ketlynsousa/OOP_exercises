# Create a structure capable of calculating the salaries of different employees.
# Employee (abstract class)
     # - Name  (attribute)
     # - Gross Salary (attribute)
     # - Net Salary (attribute)
     # - Monthly Minimum Wage = $1612 (class attribute)
     # - SSA = 7.5% (class attribute)
     # - Salary Calculation (abstract method)
     # - Analyze of Salary (concrete method)
""" Hourly-paid Worker (subclass)
        - Hourly Wage (attribute)
        - Hours Worked (attribute)
        - Salary Calculation (abstract method) """
""" Monthly-paid Worker (subclass)
    - Name (attribute)
    - Gross Salary (attribute)
    - Salary Calculation (abstract method) """

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Employee(ABC):
    monthly_minimum_wage = 1612
    SSA = 0.075
    def __init__(self, name = None):
        self.name = name
        self.gross_salary = 0
        self.net_salary = 0

    @abstractmethod
    def salary_calculation(self):
        pass

    def salary_analyze(self):
        minimum_wage_proportion:float = self.net_salary / Employee.monthly_minimum_wage

        title = 'Salary Analysis'
        content = f'Salary for the employee [blue]{self.name}[/] ([magenta]{type(self).__name__}[/]) is [green]${self.salary_calculation():.2f}[/] and corresponds to [yellow]{minimum_wage_proportion:.1f} minimum wages[/].'

        panel = Panel(content, title=title, width=50)
        print(panel)


class HourlyWorker(Employee):
    def __init__(self, name, hourly_wage = 7.37, hours_worked = 220):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.gross_salary = self.hourly_wage * hours_worked

    def salary_calculation(self):
        self.net_salary = self.gross_salary - (self.gross_salary * Employee.SSA)
        return self.net_salary
    

class MonthlyWorker(Employee):
    def __init__(self, name, gross_salary = Employee.monthly_minimum_wage):
        super().__init__(name)
        self.gross_salary = gross_salary

    def salary_calculation(self):
        self.net_salary = self.gross_salary - (self.gross_salary * Employee.SSA)
        return self.net_salary
