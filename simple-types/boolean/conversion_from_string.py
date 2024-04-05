strValue = "true"
boolValue1 = strValue.lower() == "true"
# boolValue1 is True

strValue = "false"
boolValue2 = bool(strValue)
# boolValue2 is False

boolValue3 = bool("")
# boolValue3 is False

print(str(boolValue1))
print(str(boolValue2))
print(str(boolValue3))