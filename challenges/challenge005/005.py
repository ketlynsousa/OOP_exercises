# Create a class called Gamer where we can register name, user, and favorites games of a person.
# Create as well a method that allows you to display a profile panel of this player.

from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, name='', user=''):
        self.name = name
        self.user = user
        self.favorite_games = list()

    def add_favorites(self, games):
        self.favorite_games.append(games)
        self.favorite_games.sort()

    def profile_card(self):
        title = f'Player <{self.user}>'
        content = f'Real name: {self.name}\n'
        content += f'Favorite Games: '

        for g in self.favorite_games:
            content += f'\n:video_game: [blue]{g}[/]'
        box = Panel(content, title=title, width=50)
        return print(box)

# Main Program
player1 = Gamer('Fabricio da Silva', 'detonador2025')
player1.add_favorites('Mario Bros')
player1.add_favorites('Sonic')
player1.add_favorites('God of War')
player1.add_favorites('Fortnite')
player1.profile_card()

player2 = Gamer('Olivia Souza', 'peach_raivosa')
player2.add_favorites('Mario Bros')
player2.add_favorites('Call of Duty')
player2.profile_card()
