import json

data_s = "[2, 3, 5, 7, 11]"
numbers = json.loads(data_s)

print(f"{numbers = }")
print(f"{type(numbers) = }")
