import os
from colorama import Fore, init

init(autoreset=True)

choice = int(input("Find:\n1 - directories\n2 - files\n3 - all\n"))
path = input("Path: ")
if choice == 1:
    for t in os.walk(path, "."):
        print(t[0])

elif choice == 2:
    for t in os.walk(path, "."):
        for f in t[2]:
            print(f)

else:
    for dirpath, dirnames, filenames in os.walk(path, '.'):
        print(Fore.YELLOW + str(dirpath))
        for f in filenames:
            print(f)
            print(os.path.join(dirpath, f))
        else:
            print("")