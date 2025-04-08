numbers = [2, 3, 5, 7, 11, 13, 17]
string = ""
for i in range(0, len(numbers)):
    string += str(numbers[i])
    if i < (len(numbers) - 1):
        string += "; "
# string is "2; 3; 5; 7; 11; 13; 17"
print(f"{string = }")
