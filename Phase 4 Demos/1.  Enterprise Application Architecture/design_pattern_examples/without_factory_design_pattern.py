
class UPIPayment:
    def pay(self):
        print("Payment using UPI")

class CreditCardPayment:
    def pay(self):
        print("Payment using Credit Card")


class NetBankingPayment:
    def pay(self):
        print("Payment using Net Banking")


# Client code
payment_type = "UPI"

if payment_type == "UPI":
    payment = UPIPayment()

elif payment_type == "CREDIT_CARD":
    payment = CreditCardPayment()

elif payment_type == "NET_BANKING":
    payment = NetBankingPayment()

payment.pay()