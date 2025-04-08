numbers = [2, 3, 5, 7, 11, 13, 17]
string = ""
for i in reversed(numbers):
    string = string + str(i) + "; "
# string is "17; 13; 11; 7; 5; 3; 2; "
print(f"{string = }")
