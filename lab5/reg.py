import re

string = input("Enter the sentence: ")
x = re.search(r"ab*", string)

if not x:
    print("no")
else:
    print("yes")