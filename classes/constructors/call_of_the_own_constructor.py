# In pPython class
# you cannot define multiple constructors


class Man:
    def __init__(self, name, country="unknown"):
        self.name = name
        self.country = country


man = Man("Vladimir", "Russia")

print(man.name)
print(man.country)
