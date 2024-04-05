value1 = True
value2 = False

valueNot1 = (not value1)
# valueNot1 is False

valueNot2 = (not value2)
# valueNot2 is True

valueAnd = value1 and value2
# valueAnd is False

valueOr = value1 or value2
# valueOr is True

valueXor = value1 ^ value2
# valueXor is True

print(f"{valueNot1 = }")
print(f"{valueNot2 = }")
print(f"{valueAnd = }")
print(f"{valueOr = }")
print(f"{valueXor = }")