import json


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rect:
    def __init__(self, size):
        self.size = size


class ClassEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, '__dict__'):
            return o.__dict__
        else:
            super().default(self)

rect = Rect(Size(5, 10))

data_s = json.dumps(rect, cls=ClassEncoder)

print(f"{data_s }")