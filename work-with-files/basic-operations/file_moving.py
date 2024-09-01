import shutil

file = "file.txt"
to_file = "new_file.txt"
try:
    shutil.move(file, to_file)
except Exception as e:
    print("Error: " + e.__str__())
