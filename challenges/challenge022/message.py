# Implement a standardized messaging system using object-oriented programming.
""" - Message [super class]
    - #message [protected attribute]
    - #type [protected attribute]
    - #icon [protected attribute]

    - show() [public method]  """

""" - Error [subclass] 
    - show() [public method] """

""" - Warning [subclass]
    - show() [public method]] """
from rich import print
from rich.panel import Panel


class Message:
    """
        Superclass representing a generic terminal notification message.

        Handles message text validation and default visual rendering using Rich Panel.

        Attributes:
            _message (str): Protected attribute storing the notification text.
            _type (str): Protected attribute storing the category/label of the message.
            _icon (str): Protected attribute storing the emoji/icon identifier.

        Properties:
            message (str): Getter/Setter for the notification text. Validates that
                the trimmed string is at least 5 characters long.

        Methods:
            show(): Renders and prints the formatted message panel in the terminal.
        """

    def __init__(self, txt:str='', type:str='Message', icon:str=':speech_balloon:'):
        self._message = txt
        self._type = type
        self._icon = icon

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, txt:str):
        txt = txt.strip()
        if len(txt) >= 5:
            self._message = txt
        else:
            raise TypeError('This type of message cannot be displayed.')

    def show(self):
        panel  = Panel(self.message, title=f'{self._icon} {self._type.upper()} {self._icon}', style='bold #ffffff on #000000', border_style='red', width=50)
        print(panel)


class Alert(Message):
    """
        Represents a warning or alert notification, inheriting base properties from Message.

        Overrides visual styling to display a yellow-highlighted panel with a warning icon.

        Methods:
            show(): Renders and prints the alert panel with custom warning styles.
        """

    def __init__(self, txt: str, type:str = 'alert', icon:str = ':warning:'):
        super().__init__(txt, type, icon)


    def show(self):
        panel = Panel(self._message, title=f'{self._icon} {self._type.upper()} {self._icon}', style='bold #000000 on #fffc1b', border_style='green', width=50)
        print(panel)


class Error(Message):
    """
        Represents an error notification, inheriting base properties from Message.

        Overrides visual styling to display a red-highlighted panel with a stop/no-entry icon.

        Methods:
            show(): Renders and prints the error panel with custom error styles.
        """

    def __init__(self, txt:str, type:str = 'Error', icon:str = ':no_entry_sign:'):
        super().__init__(txt, type, icon)

    def show(self):
        panel = Panel(self._message, title=f'{self._icon} {self._type.upper()} {self._icon}', style='bold #fffc1b on #880000', border_style='yellow', width=50)
        print(panel)

