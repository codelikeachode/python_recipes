class Man:
    def __init__(self, name):
        self.name = name


class Employee(Man):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position


employee = Employee("Max", "booker")

print(employee.name)
print(employee.position)
