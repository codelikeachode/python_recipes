from locale import *

# to Int
strNumber = "42"
number = int(strNumber)

# to Double and Float
# first method
strPi = "3.14"
piFloat = float(strPi)

# second method
strExp = "2.71828"
exp = atof(strExp)

# third method
strHalf = "0,5"
half = atof(strHalf.replace(',', '.'))

print(f"{number = }")
print(f"{piFloat = }")
print(f"{exp = }")
print(f"{half = }")