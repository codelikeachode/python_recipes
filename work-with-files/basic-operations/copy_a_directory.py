import os
import shutil

direct = os.path.join(os.getcwd(), "data")
direct_copy = os.path.join(os.getcwd(), "data_copy")

try:
    shutil.copytree(direct, direct_copy)
except Exception as e:
    print("Error happened " + e.__str__())
