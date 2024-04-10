file_name = "file.txt"

with open(file_name, 'r') as text_file:
    for line in text_file:
        print(line)