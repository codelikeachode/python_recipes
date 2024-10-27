import json


class Data:
    def __init__(self, text, num, arr):
        self.text = text
        self.num = num
        self.arr = arr


data = Data("Hello", 3.14, [2, 5, 7])

data_s = json.dumps(data.__dict__)
# {"text": "Hello", "num": 3.14, "arr": [2, 5, 7]}
print(f"{data_s = }")
