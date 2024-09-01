import os

file_dir = os.path.dirname(os.path.realpath(__file__))
files = [f for f in os.listdir(file_dir) if f.endswith(".txt")]

print(files)
