class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __invert__(self):
        self.x, self.y = self.y, self.x


p = Point(1, 3)
~p

print(p.x, p.y)
