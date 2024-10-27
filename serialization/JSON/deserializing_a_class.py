import json


class Data:
    def __init__(self, text, num, lst):
        self.text = text
        self.num = num
        self.lst = lst


def data_decode(dct):
    return Data(dct["text"], dct["num"], dct["lst"])


data_s = '{"text": "Hello", "num": 3.14, "lst": [2, 5, 7]}'
data = json.loads(data_s, object_hook=data_decode)

print(f"{data.text = }")
print(f"{data.num = }")
print(f"{data.lst = }")
