import shutil

file = "file.txt"
file_copy = "file_copy.txt"
try:
    shutil.copyfile(file, file_copy)

    # copy with metadata and permissions
    shutil.copy2(file, file_copy)
except Exception as e:
    print("Error: " + e.__str__())
            