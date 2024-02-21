from datetime import datetime, timedelta

# #1
# def ago5days(n):
#     ago = n - timedelta(days=5)
#     print(ago.strftime("%Y-%m-%d"))

# n = datetime.now()
# ago5days(n)

# #2
# def y_t_t(n):
#     y = n - timedelta(days=1)
#     td = n
#     tm = n + timedelta(days=1)
#     print(y.strftime("%Y-%m-%d"), td.strftime("%Y-%m-%d"), tm.strftime("%Y-%m-%d"))


# n = datetime.now()
# y_t_t(n)

#3
def no_microsec(n):
    print(n.replace(microsecond = 0))

no_microsec(datetime.now())

#4
def diff(n, m):
    dif = m - n
    print(dif.total_seconds())
n = datetime(2018, 2, 1)
m = datetime(2020, 3, 30)
diff(n, m)