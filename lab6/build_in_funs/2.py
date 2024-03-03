string = input()
print("smol: ", len([char for char in string if char.islower()]))
print("BIG: ", len([char for char in string if char.isupper()]))