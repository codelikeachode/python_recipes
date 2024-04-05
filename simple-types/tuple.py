one = (1, "one")
number = one[0]
# number is 1
str_v = one[1]
# str is "one"

twoList = [2, "two"]
two = tuple(twoList)

# two[0] = 2000 # <- Error

print(f"{number = }")
print(f"{str_v = }")
print(f"{two = }")