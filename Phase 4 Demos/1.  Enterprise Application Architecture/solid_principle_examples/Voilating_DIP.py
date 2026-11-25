class EmailService:

    def send_email(self, message):
        print("Email sent:", message)

class SMSService:

    def send_sms(self, message):
        print("SMS sent:", message)
        
class BankService:

    def __init__(self):
        self.email = EmailService()

    def notify_customer(self, message):
        self.email.send_email(message)


# Main application

bank = BankService()

bank.notify_customer("Your transaction is successful")