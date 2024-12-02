class Man:
    def __init__(self, name="unknown", country="unknown"):
        self.name = name
        self.country = country


man1 = Man()
# man1.name is "unknown"
# man1.country is "unknown"

man2 = Man("Vladimir")
# man2.name is "Vladimir"
# man2.country is "unknown"

man3 = Man(country="Brazil")
# man3.name is "unknown"
# man3.country is "Brazil"

man4 = Man("Vladimir", "Brazil")
# man4.name is "Vladimir"
# man4.country is "Brazil"

print(man1.name, man1.country)
print(man2.name, man2.country)
print(man3.name, man3.country)
print(man4.name, man4.country)
