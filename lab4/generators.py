def my_generator(n):
    value = 1
 
    while value <= n:
 
        yield value**2
        value += 1
 
for value in my_generator(3):
    print(value)