# Create a class called 'Barbecue' where you can specify how many people will be participating
# and display how much meat must be purchased and the total cost of the barbecue and the price per person.
# Standard consume 400g per person
# Meat Price: 82.40/kg

from rich.panel import Panel
from rich import print

class Barbecue:
    standard_consume:float = 0.400 # each individual will consume about 400g of meat
    total_meat_price:float = 82.40 # total Kg price of the meat
    def __init__(self, name='', quantity=0):
        self.name = name
        self.people = quantity


    def meat(self):
        return self.people * Barbecue.standard_consume

    def total_price(self) -> float:
        return self.meat() * self.total_meat_price

    def individual_price(self):
        return self.total_price() / self.people

    def analyse(self):
        content = f"""
        Analysing the [green]{self.name}[/] with [blue]{self.people} guests[/]
        Each guest will consume {Barbecue.standard_consume}Kg of meat and each Kg costs ${Barbecue.total_meat_price:.2f}
        Recommend [blue]to buy {self.meat():,.0f}kg[/] of meat for this event
        The total cost will be [green]${self.total_price():,.2f}[/]
        Each person will pay [yellow]${self.individual_price()}[/] to participate.
        """
        box = Panel(content, title=self.name)
        return print(box)

# Main Program
b1 = Barbecue('Barbecue with Friends', 15)
b1.analyse()

c2 = Barbecue('End of Year Party', 80)
c2.analyse()
