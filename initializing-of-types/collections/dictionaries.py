languages = {"sp": "spanish", "en": "english"}

numbers = {1: "one", 2: "two", 3: "three"}


class Employee:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name


employees = {1: Employee("Smith", "John"), 2: Employee("Frank", "Joe")}

print(f"{languages = }")
print(f"{numbers = }")
print(f"{employees = }")
