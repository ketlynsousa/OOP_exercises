# Create classes for data validators, using the following examples.
""" - Validator - [abstract class]
    - validate() - [method]  """

""" - Username(subclass)
Rules:
- 5 to 20 characters
- Only lowercase letters
- It can have numbers
- It can have underscores  """

""" - Email(subclass) 
Rules:
- Must contain a single @
- The username can contain letters, numbers, and some symbols
- Domains must contain a dot
- The TLD ends with a dot and at least two letters. """

""" - Password(subclass) 
Rules:
- At least 8 characters
- At least one uppercase letter
- At least one symbol """
from rich import print
from abc import ABC, abstractmethod
import re


class Validator(ABC):
    """
        Abstract base class for data validators.

        Enforces a interface for validating input string values.

        Methods:
            validate(value: str): Abstract method that must be implemented by subclasses
                to validate input strings according to specific criteria.
        """

    @abstractmethod
    def validate(self, value:str):
        pass


class Username(Validator):
    """
        Validator subclass for checking username format criteria.

        Validation Rules:
            - Length must be between 5 and 20 characters.
            - Contains only lowercase letters, digits, and underscores (`_`).

        Methods:
            validate(value: str) -> bool:
                Validates whether the provided username matches the required format rules.
        """

    def validate(self, value:str) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, value):
            return True
        else:
            return False


class Email(Validator):
    """
        Validator subclass for checking email address formats.

        Validation Rules:
            - Must contain exactly one `@` symbol separating local name and domain.
            - Username part may contain letters, numbers, and allowed punctuation (`.`, `_`, `%`, `+`, `-`).
            - Domain part must contain a valid dot and a TLD ending with at least two characters.

        Methods:
            validate(value: str) -> bool:
                Validates whether the provided email string matches standard email formatting.
        """

    def validate(self, value:str) -> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex, value):
            return True
        else:
            return False


class Password(Validator):
    """
        Validator subclass for enforcing password strength requirements.

        Validation Rules:
            - Must be at least 8 characters long.
            - Must contain at least one uppercase letter, one lowercase letter, one digit, and one special symbol (`@`, `!`, `#`, `$`, `%`, `?`).

        Methods:
            validate(value: str) -> bool:
                Validates whether the provided password meets the security strength rules.
        """

    def validate(self, value:str):
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$"
        if re.fullmatch(regex, value):
            return True
        else:
            return False


def validate_data(obj: Validator, value: str):
    """
        Executes a validation check using a Validator instance and prints the formatted result.

        Args:
            obj (Validator): An instance of a concrete `Validator` subclass.
            value (str): The string value to be validated.
        """

    result = obj.validate(value)
    print(f"Value: [yellow]{value}[/] is it valid ? {'[green]YES[/]' if result else '[red]NO[/]'}")

