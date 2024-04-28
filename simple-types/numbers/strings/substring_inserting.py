dataString = "string"

dataString = "Sub" + dataString
# dataString is "Substring"
print(dataString)

dataString = dataString + "!"
# dataString is "Substring!"
print(dataString)

dataString = dataString[:9] + "inserting" + dataString[9:]
# dataString is "Substring inserting!"
print(dataString)