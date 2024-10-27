class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __xor__(self, power):
        self.x = self.x**power
        self.y = self.y**power
        return self


p1 = Point(2, 3)
p1 = p1 ^ 3

p2 = Point(2, 3)
p2 ^ 2

print(p1.x, p1.y)
print(p2.x, p2.y)
