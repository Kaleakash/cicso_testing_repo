

# D – Dependency Inversion Principle (DIP)
# Definition: High-level modules should not depend directly on low-level modules. Both should depend on abstractions.

# In simple words:

# A business class should not be tightly connected to a particular implementation.

from abc import ABC, abstractmethod


# Abstraction
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Low-level implementations

class EmailService(Notification):

    def send(self, message):
        print("Email sent:", message)


class SMSService(Notification):

    def send(self, message):
        print("SMS sent:", message)


class WhatsAppService(Notification):

    def send(self, message):
        print("WhatsApp sent:", message)


# High-level module

class BankService:

    def __init__(self, notification):
        self.notification = notification

    def notify_customer(self, message):
        self.notification.send(message)


# Main application

#notification = SMSService()
#notification = WhatsAppService()
notification = EmailService()

bank = BankService(notification)

bank.notify_customer("Your transaction is successful")