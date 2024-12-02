class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Point:
    def __init__(self, top, left):
        self.top = top
        self.left = left


class Rectangle:
    def __init__(self, p_size, p_point):
        self.size = p_size
        self.point = p_point


size = Size(10, 10)
point = Point(5, 5)
rect = Rectangle(size, point)

print(rect.point.left)
