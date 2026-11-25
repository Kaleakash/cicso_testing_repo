from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Credit Card payment:", amount)
        
class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI payment:", amount)
class NetBankingPayment(Payment):

    def pay(self, amount):
        print("Net Banking payment:", amount)
class WalletPayment(Payment):

    def pay(self, amount):
        print("Wallet payment:", amount)


# Main application

payments = [
    UPIPayment(),
    CreditCardPayment(),
    WalletPayment()
]

for payment in payments:
    payment.pay(2000)