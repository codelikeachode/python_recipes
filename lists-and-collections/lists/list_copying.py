import copy

numbers1 = [1, 2, 3, 4, 5]

# the first method
numbers2 = list(numbers1)

# the second method
numbers3 = numbers1[:]

# the third method with deep copy
numbers4 = copy.deepcopy(numbers1)

print("numbers1 id = " + str(id(numbers1)))
print("numbers2 id = " + str(id(numbers2)))
print(numbers2)
print("numbers3 id = " + str(id(numbers3)))
print(numbers3)
print("numbers4 id = " + str(id(numbers4)))
print(numbers4)