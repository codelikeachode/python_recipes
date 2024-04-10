file_name = "file.txt"

with open(file_name, 'r') as text_file:
    text = text_file.read()
    print(text)