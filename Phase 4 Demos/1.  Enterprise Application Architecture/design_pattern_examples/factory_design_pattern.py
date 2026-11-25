
# provide super Payment abstract class and all sub class inherit from it
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):

    def pay(self):
        print("Payment using UPI")


class CreditCardPayment(Payment):

    def pay(self):
        print("Payment using Credit Card")


class NetBankingPayment(Payment):

    def pay(self):
        print("Payment using Net Banking")

# Factory class to create payment objects based on payment type
class PaymentFactory:
    @staticmethod
    def get_payment(payment_type):

        if payment_type == "UPI":
            return UPIPayment()

        elif payment_type == "CREDIT_CARD":
            return CreditCardPayment()

        elif payment_type == "NET_BANKING":
            return NetBankingPayment()

        else:
            raise ValueError("Invalid payment type")


# Client code
payment_type = "UPI"
payment = PaymentFactory.get_payment(payment_type)
payment.pay()




