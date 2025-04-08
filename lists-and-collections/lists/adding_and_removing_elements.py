primeNumbers = [2, 5, 7]
print(primeNumbers)
primeNumbers.append(11)
# primeNumbers is [2, 5, 7, 11]
print(primeNumbers)
primeNumbers.insert(1, 3)
# primeNumbers is [2, 3, 5, 7, 11]
print(primeNumbers)
primeNumbers.remove(2)
# primeNumbers is [3, 5, 7, 11]
print(primeNumbers)
del primeNumbers[1]
# primeNumbers is [3, 7, 11]
print(primeNumbers)
primeNumbers.extend([13, 17])
# primeNumbers is [3, 7, 11, 13, 17]
print(primeNumbers)
primeNumbers.clear()
# primeNumbers is []
print(primeNumbers)
