class Phone:
    def __init__(self, model):
        self.model = model


class Employee:
    def __init__(self, first_name, last_name, personal_phone):
        self.firstName = first_name
        self.lastName = last_name
        self.personalPhone = personal_phone


nokiaPhone = Phone("Nokia 6610")
kim = Employee("Victoria", "Kim", Phone("iPhone 5"))

print(kim.firstName)
