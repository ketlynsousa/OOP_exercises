# Create a class called 'Book' that it will simulate the turning page of a book,
# also consider if the user got to the end of the reading.

from rich import print
from time import sleep

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.total_pages = pages
        self.current_page = 1

        print(f':open_book: [blue]You just opened the book [green]"{self.title}"[/] with [yellow]{self.total_pages} pages[/] in total. You are currently at the [yellow]page {self.current_page}.[/]')

    def turn_page(self, qtd=1):
        count = 0
        for pg in range(0, qtd, 1):
            if not self.end_page():
                self.current_page += 1
                print(f'Page{self.current_page} ➡ ', end='')
                sleep(0.4)
                count +=1
        print(f'[blue]You advanced [yellow]{count} pages[/] and is currently at the [yellow]page {self.current_page}.[/]')
        if self.end_page():
            print(f':closed_book: [red]You got to the end of the book.[/]')

    def end_page(self):
        return True if self.current_page == self.total_pages else False


# Main Program
b1 = Book('10 Things I Learned', 20)
b1.turn_page(5)
b1.turn_page(10)
b1.turn_page(50)
