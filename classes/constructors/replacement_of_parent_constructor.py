class Man:
    def __init__(self, name):
        self.name = name


class Employee(Man):
    def __init__(self, name):
        super().__init__(name)
        self.position = "unknown"


employee = Employee("Max")

print(employee.name)
print(employee.position0)
