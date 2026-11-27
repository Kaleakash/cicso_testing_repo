class ValidAgeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)  # set the message to super class ie Exception 
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValidAgeException("Age cannot be negative")
    elif age < 18:
        raise ValidAgeException("Age must be at least 18")
    else:
        print("Age is valid")
except ValidAgeException as e:
    print("Exception details:", e)


print("Program executed successfully")