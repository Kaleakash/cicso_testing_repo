class EmailService:
    def send_email(self, message):
        print("Email sent:", message)

class BankService:
    def __init__(self):
        # Creating dependency internally
        self.email = EmailService()

    def transfer_money(self, amount):
        print("Money transferred:", amount)

        self.email.send_email(
            "Transaction successful"
        )


# Main application

bank = BankService()

bank.transfer_money(5000)