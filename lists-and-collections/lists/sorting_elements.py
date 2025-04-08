numbers = [11, 2, 5, 7, 3]
numbers.sort()
# numbers is [2, 3, 5, 7, 11]
print(f"{numbers = }")
# descending
numbers.sort(reverse=True)
# numbers is [11, 7, 5, 3, 2]
print(f"{numbers = }")
lst = [["B", 3], ["A", 2], ["C", 1]]
lst.sort(key=lambda i: i[0])
# arr is [['A', 2], ['B', 3], ['C', 1]]
print(f"{lst = }")
lst.sort(key=lambda i: i[1], reverse=True)
# arr is [['B', 3], ['A', 2], ['C', 1]]
print(f"{lst = }")
