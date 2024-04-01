from random import randint

def get_monitor_size():
    return randint(14, 27)

str_v = ""
inch_size = get_monitor_size()
match inch_size:
    case 14 | 15:
        str_v = "way to small"
    case 16 | 17 | 18:
        str_v = "ok for light work"
    case 19 | 20 | 21 | 22 | 23:
        str_v = "good for office work"
    case 24 | 25 | 26 | 27:
        str_v = "perfect size for all work types"

print(f"Monitor {inch_size} is {str_v}")