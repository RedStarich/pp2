# #1
# def square(N):
#     value = 1
 
#     while value <= N:
 
#         yield value**2
#         value += 1
 
# N = 3
# for value in square(N):
#     print(value)

# #####################################
# #2
# def even_nums(n):
#     value = 0
#     res = []
 
#     while value <= n:
#         if value%2==0:
#             res.append(value)
#         value += 1
#     yield res
# n = int(input("Enter the number"))
# for value in even_nums(n):
#     print (', '.join(map(str, value)))
# ##############################################
# #3
    
# def div_by_3_and_4(n):

#     value = 0

#     while value <= n:

#         if value%3==0 or value%4==0:
#             yield value

#         value += 1
    
# n = 5
# for value in div_by_3_and_4(n):
#     print(value)
# ########################################
# #4
# def squares(a, b):

#     res = []

#     while a <= b:

#         yield a**2
#         a += 1
# a = 5
# b = 10
# for value in squares(a, b):
#     print(value)
###########################################
#5
def rever(n):
    value = n;
    while  value >= 0:

        yield value
        value -= 1
n = 5
for value in rever(n):
    print(value)