# in Python, you can't change param reference
class Swap:
    @staticmethod
    def strings(v1: list[str], v2: list[str]):
        v1[0], v2[0] = v2[0], v1[0]


s1 = ["A"]
s2 = ["B"]
Swap.strings(s1, s2)
# s1[0] is "B", s2[0] is "A"

print(s1)
print(s2)
