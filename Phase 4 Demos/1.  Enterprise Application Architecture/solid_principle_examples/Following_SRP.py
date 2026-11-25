class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:

    def calculate(self, employee):
        return employee.salary

class EmailService:

    def send_email(self, employee):
        print("Email sent to", employee.name)

class ReportGenerator:

    def generate(self, employee):
        print("Generating report for", employee.name)


# Main application
emp = Employee("Akash", 50000)

salary = SalaryCalculator()
email = EmailService()
report = ReportGenerator()

print(salary.calculate(emp))

email.send_email(emp)

report.generate(emp)