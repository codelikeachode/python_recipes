import os

file_name = "file_copy.txt"
try:
    os.remove(file_name)
except Exception as e:
    print("Error happened " + e.__str__())
