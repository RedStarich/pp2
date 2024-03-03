f = open("test_write.txt", "w")
li = input("List nums with comma: ").split(", ")
f.write(str(li))
f.close()