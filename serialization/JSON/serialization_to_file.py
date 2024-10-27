import json


class Data:
    def __init__(self, text, num, arr):
        self.text = text
        self.num = num
        self.arr = arr


data = Data("Hello", 3.14, [2, 5, 7])

with open("data.json", "w") as f:
    json.dump(data.__dict__, f)
