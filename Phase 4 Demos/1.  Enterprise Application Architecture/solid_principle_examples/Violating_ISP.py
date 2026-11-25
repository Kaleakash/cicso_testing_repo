class Printer:
    def print_document(self):
        pass
    def scan_document(self):
        pass
    def fax_document(self):
        pass
    
class SimplePrinter(Printer):
    def print_document(self):
        print("Printing document")
    def scan_document(self):
        raise NotImplementedError
    def fax_document(self):
        raise NotImplementedError

class AdvancedPrinter(Printer):

    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Sending fax")

        
# Main application

simple_printer = SimplePrinter()
advanced_printer = AdvancedPrinter()

simple_printer.print_document()
simple_printer.scan_document()
advanced_printer.print_document()
advanced_printer.scan_document()
advanced_printer.fax_document()