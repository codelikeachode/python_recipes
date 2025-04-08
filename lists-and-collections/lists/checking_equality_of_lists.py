n1 = [1, 2, 3]
n2 = [1, 2, 3]
n3 = [3, 2, 1]
equal1 = n1 == n2
# equal1 is True
equal2 = n1 == n3
# equal2 is False
equal3 = set(n1) == set(n3)
# equal3 is True
print(f"{equal1 = }")
print(f"{equal2 = }")
print(f"{equal3 = }")
