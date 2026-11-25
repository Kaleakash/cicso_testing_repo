class Payment:

    def pay(self, payment_type, amount):

        if payment_type == "credit_card":
            print("Credit Card payment:", amount)

        elif payment_type == "upi":
            print("UPI payment:", amount)

        elif payment_type == "net_banking":
            print("Net Banking payment:", amount)


payment = Payment()

payment.pay("upi", 2000)