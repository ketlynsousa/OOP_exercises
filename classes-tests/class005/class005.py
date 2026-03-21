# Creating a class called Meal where I can add the price of each element of it and calculate how much cost the meal to prepare and per day
from rich import print

class Meal:
    def __init__(self, protein, carbohydrate, vegetables):
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.vegetables = vegetables

    def total_price(self):
        return self.protein + self.carbohydrate + self.vegetables

    def summary(self, day):
        print(f'Total price for {day.title()} meal is [green]${self.total_price():.2f}[/]')

    def proportion(self, amount_days):
        result = self.total_price() / amount_days
        print(f'For {amount_days} days meal. Each day costed [green]${result:.2f}[/]')


# Main Program
monday_meal = Meal(7.50, 1.20, 3.10)
monday_meal.summary('monday')
monday_meal.proportion(3)
