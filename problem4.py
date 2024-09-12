import os

# Specify the directory you want to list
directory_path = '/Aadi Python'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for items in contents:
    print(items)