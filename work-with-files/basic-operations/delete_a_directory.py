import os

directory = os.path.join(os.getcwd(), "data")

try:
    os.rmdir(directory)
except Exception as e:
    print("Error happened " + e.__str__())
