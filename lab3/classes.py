# class First():
#     def getString():
#         my_str = input("Enter the string: ")
#         return my_str
#     element = getString()
#     def print_String(element):
#         element = element.upper()
#         print(element)

#     print_String(element)

# class Shape():
#     def __init__(self, area):
#         self.area = area

#     def calculate_area(self, length, width):
#         s = length*width
#         print(s)
#         return s
    
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__(area=0)
#         self.length = length
#         self.calculate_area(self.length, self.length)
# l = int(input("Enter length: "))
# square = Square(l)

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(area=0)
#         self.length = length
#         self.width = width
#         self.calculate_area(self.length, self.width)
# l = int(input("Enter length: "))
# w = int(input("Enter width: "))
# square = Rectangle(l, w)

# class Point():
#     x = input("Enter x: ")
#     y = input("Enter y: ")
#     x = int(x)
#     y = int(y)

#     def show(x, y):
#         print(x, ":", y)

#     def move(x, y):
#         new_x = input("change x: ")
#         new_y = input("change y: ")
#         x = int(new_x)
#         y = int(new_y)
#         return x, y

#     def dist(x1, y1, x2, y2):
#         import math
#         x2 = int(input("Enter second point's x: "))
#         y2 = int(input("Enter second point's y: "))
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#         return distance
    
#     print(dist(x, y, 2, 3))

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        sum = int(input("Enter the sum you want to put: "))
        self.balance += sum
        return self.balance

    def withdraw(self):
        cash = (int(input("Enter how much you want to withdraw: ")))
        if self.balance < cash:
            print("not enough money on the balance")
            return self.balance
        else:
            print("success")
            self.balance -= cash
            return self.balance
        
account = Account(owner="John Doe", balance=1000)
account.deposit()
account.withdraw()
account.withdraw()


class Filterprime():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    print(filtered_numbers)

