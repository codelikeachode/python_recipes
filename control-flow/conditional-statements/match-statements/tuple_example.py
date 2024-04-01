def get_point():
    return 5, 5

str_v = ""
point = get_point()

match point:
    case (0, 0):
        str_v = "(0, 0) point"
    case (_, 1):
        str_v = f"(_, 1), y == 1"
    case (1, y):
        str_v = f"(1, {y}), x == 1"
    case x, y if x == y:
        str_v = f"({x}, {y}), x == y"
    case _:
        str_v = "Some other point"

print(f"{str_v = }")