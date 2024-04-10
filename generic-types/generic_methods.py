from typing import TypeVar
T = TypeVar('T')

def swap(v1: list[T], v2: list[T]):
    v1[0], v2[0] = v2[0], v1[0]
    
n1 = [5]
n2 = [7]
swap(n1, n2)

s1 = ["cat"]
s2 = ["dog"]
swap(s1, s2)

print(f'{n1 = }, {n2 = }')
print(f'{s1 = }, {s2 = }')