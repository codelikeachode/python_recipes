import json

data_s = '{"1": "one", "2": "two"}'

dic = json.loads(data_s)

print(f"{dic = }")
print(f"{type(dic) = }")
