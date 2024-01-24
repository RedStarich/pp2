#task1
class Solution:
    grams = input("enter mass in grams")
    def to_ounces(grams):
        ounces = 28.3495231 * grams
        return ounces

#task2
class Solution:
    F = input("Enter temperature in Fahrenheit")
    def Fahrenheit_to_Celsius(F):
        C = (5 / 9) * (F - 32)
        return C

#task3
class Solution:
    heads = 35
    legs = 94
    
    def solve(heads, legs):
        rabbits = 0
        chickens = 0
        chickens = 2 * heads - 0.5 * legs
        '''
            heads = rabbits + chickens
            4 * rabbits = (legs - 2*chickens)
            rabbits = 1/4(legs - 2*chickens)
            rabbits = heads - chickens
            heads - chickens = 1/4 (legs - 2*chickens)
            chickens = heads - (1/4)legs + (1/2)chickens
            (1/2)chickens = heads - (1/4)legs
            chickens = 2*heads - (1/2)legs
        '''
        rabbits = heads - chickens
        print("rabbit count = ", rabbits, "chicken count = ", chickens)

    solve(heads, legs)

#task4
class Solution:
    nums = []
    def filter_prime(nums):
        ans = []
        for num in nums:
            for i in range(2, num/2):
                is_prime = True

                if num%i == 0:
                    is_prime = False
            if (is_prime):
                ans.append(num)
        return ans
