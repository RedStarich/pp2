import os

path = "C:\Users\Admin\Desktop\desctop\KBTU 1\codewars\pp2\lab6\test_delete.txt"

if os.access(path, os.F_OK):
    print(f"readeable: {os.access(path, os.R_OK)}\n writeable: {os.access(path, os.W_OK)}")
    os.remove(path)
    print("Success")