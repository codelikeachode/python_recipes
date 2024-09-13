# list of integer
primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]

# list of string
gameList = ["soccer", "hockey", "basketball"]


# list of Employee
class Employee:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name


employees = [Employee("Smith", "John"), Employee("Frank", "Joe")]

print(f"{primeNumbers = }")
print(f"{gameList = }")
print(f"{employees = }")
