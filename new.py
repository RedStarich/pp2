# import re
# string = "Happpy Birthday"
# x = re.compile(r"pp{1}")
# print(x.findall(string))

import os

path = "C:\Users\Admin\Desktop\desctop\KBTU 1\codewars\pp2>"
os.walk(path)
file = os.open("test.txt")
os.write("Happy Birthday" * 5)