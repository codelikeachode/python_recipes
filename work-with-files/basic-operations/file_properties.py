import os
import time

# get the directory path of the currently executing script
dir_path = os.getcwd()

# Combine the directory path with "file.txt" to create the full path to the file.
file_path = os.path.join(
    dir_path, "file.txt")

# file size
file_size = os.path.getsize(file_path)

# file modification date
date_modified = time.ctime(
    os.path.getmtime(file_path))

# is readable file
is_readable = os.access(file_path, os.R_OK)

# is writable file
is_writable = os.access(file_path, os.W_OK)

# file name and extension
name_only, extension = os.path.splitext(
    os.path.basename(file_path))

# file directory
file_dir = os.path.dirname(file_path)