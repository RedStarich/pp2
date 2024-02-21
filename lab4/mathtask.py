import math

#1
def deg_to_rad(n):
    rads = n * math.pi / 180
    print(rads)
    return rads
n = 15
deg_to_rad(n)
##################################
#2
def trapezoid_area(h, b1, b2):
    res = h * (b1+b2)/2
    print(res)
    return res

h = 5
b1 = 5
h2 = 6
trapezoid_area(h, b1, h2)
#################################
#3
def polygon_area(n, l):
    area = (n * l**2)/(4*math.tan(math.pi/n))
    print(area)

n = 3
l = 10
polygon_area(n, l)
#4
def parallelogram(l, h):
    area = l*h
    area = float(area)
    print(area)

l = 5
h = 6
parallelogram(l, h)