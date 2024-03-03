with open("test_a.txt", "r") as t1, open("test_b.txt", "a") as t2:
    for line in t1:
        t2.write(line)