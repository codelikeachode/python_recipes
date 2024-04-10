import os
import time

dir_path = os.path.dirname(
    os.path.realpath(__file__))
file_path = os.path.join(
    dir_path, "file.txt")

# file size
file_size = os.path.getsize(file_path)

# file modification time
date_modified = time.ctime(
    os.path.getmtime(file_path))

# file creation time
creation_date = time.ctime(
    os.path.getctime(file_path))

# is readable file
is_readable = os.access(file_path, os.R_OK)

# is writable file
is_writable = os.access(file_path, os.W_OK)

# file name and extension
name_only, extension = os.path.splitext(
    os.path.basename(file_path))

# file directory
file_dir = os.path.dirname(file_path)