a = 5  # 0101
b = 6  # 0110

# And
c1 = a & b
# c1 is 4 (0100)

# Or
c2 = a | b
# c2 is 7 (0111)

# Xor
c3 = a ^ b
# c3 is 3 (0011)

# shift right
c4 = a >> 1
# c4 is 2 (0010)

# shift left
c5 = b << 1
# c5 is 12 (1100)

# bits inversion
c6 = ~b
# c6 is -7 (-111)

print("{0:d}: {0:b}".format(c1, c1))
print("{0:d}: {0:b}".format(c2, c2))
print("{0:d}: {0:b}".format(c3, c3))
print("{0:d}: {0:b}".format(c4, c4))
print("{0:d}: {0:b}".format(c5, c5))
print("{0:d}: {0:b}".format(c6, c6))