class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def send_email(self):
        print("Sending employee email")

    def generate_report(self):
        print("Generating employee report")


emp = Employee("Akash", 50000)

print(emp.calculate_salary())
emp.send_email()
emp.generate_report()