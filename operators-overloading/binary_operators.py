class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2

p3 += Point(3, 5)

print(p3.x, p3.y)
