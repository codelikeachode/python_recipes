numbers = [1, 2, 3, 4, 5]
all_less10 = all(i <= 10 for i in numbers)
# all_less10 is True
some_more3 = any(i > 3 for i in numbers)
# some_more3 is True
all_odd = all(i % 2 == 1 for i in numbers)
# allOdd is False
print(f"{all_less10 = }")
print(f"{some_more3 = }")
print(f"{all_odd = }")
