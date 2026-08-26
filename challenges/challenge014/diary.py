# Simulate an object-oriented secret diary.
"""
    - Diary (class)
 - __secrets = [] {attribute}
 - __password {attribute}

 - write(msg) {method} Any person can write
 - read(password) {method} It should only be possible to read with a password
"""
from rich import print


class Diary:
    def __init__(self, password='Cev2@!'):
        self.__secrets = []
        self.__password = password.strip()

    @property
    def password(self):
        raise PermissionError('No one is permitted to see the password.')

    def write(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__secrets.append(msg.strip())

    def read(self, code=None):
        if code == self.__password:
            print(f'[green]Diary UNLOCKED![/]')
            for msg in self.__secrets:
                print(f' - {msg}')
        else:
            raise PermissionError('[red]Invalid password; you cannot read my diary.[/]')
