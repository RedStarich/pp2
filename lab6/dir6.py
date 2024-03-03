from string import ascii_uppercase
import os

new_path = "C:\Users\Admin\Desktop\desctop\KBTU 1\codewars\pp2\lab6"
if not os.access(new_path, os.F_OK):
    os.makedirs(new_path)

for letter in ascii_uppercase:
    f = open(f"{new_path}\\{letter}.txt", "w")
    f.write(f"This is {letter}'s txt file")
    f.close()