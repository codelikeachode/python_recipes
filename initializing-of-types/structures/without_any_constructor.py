# Python has no structures
class Size:
    width = 0
    height = 0


class Point:
    top = 0
    left = 0


class Rectangle:
    size = Size()
    point = Point()


rect = Rectangle()
rect.size.width = 10
rect.size.height = 10
rect.point.top = 5
rect.point.left = 5

print(rect.point.left)
