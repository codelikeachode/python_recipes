from enum import Enum

class PreciousMetal(Enum):
    Platinum = 1
    Gold = 2
    Silver = 3


class Season(Enum):
    Summer, Fall, Winter, Spring = range(4)

Planet = Enum('Planet', 'Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune')

gold = PreciousMetal.Gold
fall = Season.Fall
earth = Planet.Earth

print(f"{gold = }")
print(f"{fall = }")
print(f"{earth = }")