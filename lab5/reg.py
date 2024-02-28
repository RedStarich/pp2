import re
#1
string = input("Enter the sentence: ")
# x = re.compile(r"ab*")

#2
# x = re.compile(r"ab{2,3}")

#3
# x = re.compile(r"[a-z]_[a-z]")

#4
# x = re.compile(r"[A-Z][a-z]")

#5
# x = re.compile(r"a[a-z]*b$")          #uncomment the code to run

# print(x.findall(string))              #uncomment this line to run tasks 1-5

#6
# x = re.sub(r'[\s, \.]', string=string, repl=":")
#7
# x = re.split('_+', string)
# x = x[0].lower() + "".join(map(lambda a: a.title(), x[1:]))
#8
# x = re.split("[A-Z]", string)
# x = " ".join(x)
#9
# x = re.split("[A-Z]", string)
# x = " ".join(x)
#10
x =  re.sub(r'_([a-z])', lambda match: match.group(1).upper(), string)
print(x)