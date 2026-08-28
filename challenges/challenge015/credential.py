# Create a class that manages the SHA-256 hash of a password.
"""
 - Credential {class}
 - __hash {attribute}
 - @password {validated attribute}

 - validate(key) {method}
"""
from hashlib import sha256
from rich import print


class Credential:
    def __init__(self):
        self.__hash = None

    @property
    def password(self):
        return self.__hash

    @password.setter
    def password(self, key):
        if len(key.strip()) > 0:
            self.__hash = sha256(key.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Invalid password!')

    def validate(self, key) -> bool:
        user = sha256(key.strip().encode('utf-8')).hexdigest()
        if user == self.__hash:
            print(f'[green]Correct password![/]')
            return True
        else:
            print(f'[red]Incorrect password![/]')
            return False
