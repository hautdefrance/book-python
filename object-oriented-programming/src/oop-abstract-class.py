from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def display(self):
        with open(self.filename) as file:
            return file.read()


class PDFDocument(Document):
    def display(self):
        content = super().display()
        # display ``content`` as PDF Document


class WordDocument(Document):
    def display(self):
        content = self.display()
        # display ``content`` as Word Document


file1 = PDFDocument('filename.pdf')
file1.display()

file2 = Document('filename.txt')  # TypeError: Can't instantiate abstract class Document with abstract methods display
