import os

directory = os.path.join(os.getcwd(), "data")

if not os.path.exists(directory):
    os.makedirs(directory)