class Phone:
    model = ""


class Employee:
    firstName = ""
    lastName = ""
    personalPhone = Phone


nokiaPhone = Phone()
nokiaPhone.model = "Nokia 6610"

iPhone5 = Phone()
iPhone5.model = "iPhone 5"

kim = Employee()
kim.firstName = "Victoria"
kim.lastName = "Kim"
kim.personalPhone = iPhone5

print(kim.personalPhone.model)
print(nokiaPhone.model)
