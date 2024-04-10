file_name = "file.txt"
text = "Line 1\nLine 2"

with open(file_name, "w") as text_file:
    print(text, file=text_file)