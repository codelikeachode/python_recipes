numbers = [1, 2, 3, 4, 5]
numbers = [x * 3 for x in numbers]
# numbers is [3, 6, 9, 12, 15]
print(f"{numbers = }")
numbers = list(map(lambda x: x * 2, numbers))
# numbers is [6, 12, 18, 24, 30]
print(f"{numbers = }")
