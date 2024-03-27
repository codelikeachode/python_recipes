ar1 = [1, 2, 4, 3]
ar2 = [1, 2, 3, 4, 5]

diff = set(ar2) - set(ar1)
# diff is {5}
print("diff is", diff)