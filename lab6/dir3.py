import os

path1 = input("Path 1: ")

if os.access(path1, os.F_OK):
    print(f"Path {path1} exist")
    if os.path.isfile(path1):
        print(f"Directories: {os.path.dirname(path1)}")
        print(f"Filename: {os.path.basename(path1)}")
    else:
        print(f"directory: {path1}")
else:
    print(f"no path for {path1}")