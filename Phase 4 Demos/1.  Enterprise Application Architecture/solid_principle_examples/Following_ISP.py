from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass
class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass
class Faxable(ABC):
    @abstractmethod
    def fax_document(self):
        pass

class SimplePrinter(Printable):
    def print_document(self):
        print("Printing document")


class AdvancedPrinter(Printable, Scannable, Faxable):

    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Sending fax")


# Main application

printer1 = SimplePrinter()
printer2 = AdvancedPrinter()

printer1.print_document()

printer2.print_document()
printer2.scan_document()
printer2.fax_document()