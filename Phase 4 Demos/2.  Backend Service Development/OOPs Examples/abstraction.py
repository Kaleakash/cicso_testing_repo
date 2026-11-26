# Example of abstraction in Python using abstract base class
# using base class as Bank and sub class must be implement its abstract methods
# those classes must be SBI and HDFC

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self,acc_no):
        pass

class SBI(Bank):
    def get_interest_rate(self, acc_no):
        return "your account number " + str(acc_no) + " has interest rate " + str(7.5)

class HDFC(Bank):
    def get_interest_rate(self, acc_no):
        return "your account number " + str(acc_no) + " has interest rate " + str(8.0)

# Example usage
sbi = SBI()
hdfc = HDFC()
print(f"SBI Interest Rate: {sbi.get_interest_rate(12345)}")
print(f"HDFC Interest Rate: {hdfc.get_interest_rate(12345)}")
