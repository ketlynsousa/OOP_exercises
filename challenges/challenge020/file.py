# Create a simulator that manages the opening of different files.
""" - Files [abstract class]
    - +name [public attribute]
    - #_extension [protected attribute]
    - +size in bytes [public attribute]
    - +@full_name [validated attribute]

    - open() [abstract method]"""
""" - PDF [subclass]
    - open_file() """

""" - DOC [subclass]
    - open_file() """

from abc import ABC, abstractmethod


class File(ABC):
    """
        Abstract base class representing a generic file.

        Handles general file metadata such as name, size in bytes, and validated extensions.

        Attributes:
            name (str): Public attribute storing the file name.
            size (float | int): Public attribute storing the file size in bytes.
            _extension (str): Protected attribute storing the validated file extension.

        Properties:
            extension (str): Getter/Setter for the file extension. Validates against allowed
                formats ('pdf', 'doc', 'docx').
            full_name (str): Read-only property returning the formatted file name with its
                extension and size converted to megabytes (MB).

        Methods:
            open(): Abstract method that must be implemented by subclasses to simulate
                opening the file.
        """

    def __init__(self, name:str, size:float|int, extension:str):
        self.name = name
        self.size = size
        self._extension = None
        self.extension = extension

    @abstractmethod
    def open(self):
        pass

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, ext):
        formats = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formats:
            self._extension = ext
        else:
            raise AttributeError('This format files is not supported.')

    @property
    def full_name(self):
        size_mb = self.size / 1e+6
        return f'{self.name}.{self._extension} ({size_mb}MB)'


class PDF(File):
    """
        Represents a PDF document, inheriting base file attributes from File.

        Automatically sets the file extension to 'pdf'.

        Methods:
            open(): Simulates opening the PDF file using Adobe Reader.
        """

    def __init__(self, name:str, size:float|int):
        super().__init__(name, size, 'pdf')


    def open(self):
        print(f'Opening the file "{self.full_name}" in Adobe Reader.')


class DOC(File):
    """
        Represents a Word document, inheriting base file attributes from File.

        Automatically sets the file extension to 'docx'.

        Methods:
            open(): Simulates opening the DOC file using Microsoft Word.
        """

    def __init__(self, name:str, size:float|int):
        super().__init__(name, size, 'docx')

    def open(self):
        print(f'Opening the file "{self.full_name}" in Microsoft Word.')


# DUCK TYPING

def open_file(file:object):
    """
        Demonstrates duck typing by calling the `open()` method on any object passed.

        Args:
            file (object): An object expected to implement an `open()` method.
                If the object lacks an `open()` method or raises an exception during execution,
                an error message is printed.
        """

    try:
        file.open()
    except:
         print(f'I had a problem trying to open the file {file.__class__.__name__}')

