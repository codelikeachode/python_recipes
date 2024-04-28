import os
import shutil

directory = os.path.join(os.getcwd(), "data")

try:
    shutil.rmtree(directory)
except Exception as e:
    print("Error happened " + e.__str__())