from abc import ABC

class PUID(ABC):
    id = 0

class Named(ABC):
    name = ""

class Flower(Named):
    def __init__(self, name):
        self.name = name

rose = Flower("Rose")
isPUID = isinstance(rose, PUID)
# isPId is False

isNamed = isinstance(rose, Named)
# isNamed is True

print(isPUID)
print(isNamed)