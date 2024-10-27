import json


class Data:
    def __init__(self, text, num, lst):
        self.text = text
        self.num = num
        self.lst = lst


data = Data("Hello", 3.14, [2, 5, 7])

data_s = json.dumps(data.__dict__, indent=4)

print(f"{data_s = }")
