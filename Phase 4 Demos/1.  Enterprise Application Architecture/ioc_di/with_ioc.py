class EmailService:
    def send(self, message):
        print("Email sent:", message)
class SMSService:
    def send(self, message):
        print("SMS sent:", message)


class BankService:

    def __init__(self, notification):

        # Dependency injected from outside
        self.notification = notification

    def transfer_money(self, amount):

        print("Money transferred:", amount)

        self.notification.send(
            "Transaction successful"
        )

# Main application

#email = EmailService()
sms = SMSService()
bank = BankService(sms)

bank.transfer_money(5000)