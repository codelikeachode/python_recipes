import sys
from typing import Final

# "Final" for constants

# int
number: int = 42
otherNumber = 37
maxInt = sys.maxsize
MB: Final = 1048576

# Float
exp: float = 2.71828
billion = 1E+9

# String
greeting: Final[str] = "Hello"

# Multiline string
text1 = "this is some\n" + \
        "multiLine text"

text2: str = """this is some
multiLine text"""

text3 = ("this is some\n"
        "multiLine text")

# Bool
sunIsStar = True
earthIsStar = False

# Character "A"
charA = 'A'  # '\u0041', chr(65);

# Tuple (Int, String)
one = (1, "one")

print(f"{number = }")
print(f"{otherNumber = }")
print(f"{maxInt = }")
print(f"{MB = }")
print(f"{exp = }")
print(f"{billion = }")
print(f"{greeting = }")
print(f"{text1 = }")
print(f"{text2 = }")
print(f"{text3 = }")
print(f"{sunIsStar = }")
print(f"{earthIsStar = }")
print(f"{charA = }")
print(f"{one = }")
