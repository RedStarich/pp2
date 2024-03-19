#from datetime import datetime, timedelta
#timedelta(days=1)
#datetime.now()
#n.replace(millisecond=0)
#n.total_seconds()
#n = datetime(2018, 1, 1)
#print(n.strftime("%Y-%m-%d"))


#def fun():
    #yield 1
#for num in fun:
    #print(num)

#math.pi
#math.tan(math.pi/2)


import re
string = "22222223322332222222222"
ans = []

for i in range (1, 10):

    tmp = f"{i}{i}"
    x = re.compile(rf"{tmp}*")
    ans.append( x.findall(string))
    x.split("[A-Z]", string)
print(ans)



# import os

# now_path = os.getcwd()

# os.makedirs('General')



# os.chdir('General')
# now_path = os.getcwd()

# for i in range(1, 6):
#     os.makedirs(f'f{i}')
    
#     os.chdir(f'f{i}')
    
#     with open(f'f{i}.txt', 'w') as file:
#         file.write(f'This is file {i} in folder {f'f{i}'}')
#     os.chdir(now_path)


# import json

# with open('test.json') as f:
#     data = json.load(f)

# data_main = data ["data"]
# for entry in data_main:
#     print(entry["one"]["a1"])
