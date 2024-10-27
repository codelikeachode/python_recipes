class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return \
            self.x < other.x and \
            self.y < other.y
    
    def __gt__(self, other):
        return \
            self.x > other.x and \
            self.y > other.y
    
p1 = Point(1, 2)
p2 = Point(2, 3)

b1 = p1 > p2

b2 = p1 < p2

print(b1)
print(b2)