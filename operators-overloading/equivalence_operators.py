class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(1, 1)

equal1 = p1 == p2

equal2 = p1 == p3

equal3 = p1 != p3

print(equal1)
print(equal2)
print(equal3)
