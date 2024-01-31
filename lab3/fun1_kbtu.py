#task1
class Solution:
    
    def to_ounces(grams):
        ounces = 28.3495231 * grams
        print(ounces)
    
    grams = input("enter mass in grams: ")
    grams = int(grams)
    to_ounces(grams)

#task2
class Solution:
    
    def Fahrenheit_to_Celsius(F):
        C = (5 / 9) * (F - 32)
        print(C)
    F = input("Enter temperature in Fahrenheit: ")
    F = int(F)
    Fahrenheit_to_Celsius(F)

#task3
class Solution:
    
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

    heads = 35
    legs = 94

    solve(heads, legs)

#task4
class Solution:
    
    def filter_prime(nums):
        ans = []

        for num in nums:

            is_prime = True

            for i in range(2, num//2+1):

                if num%i == 0:
                    is_prime = False

            if (is_prime):
                ans.append(num)
        for a in ans:
            print(a)
    
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    filter_prime(nums)

#task 5
import itertools
class Solution:
    def do_permutation(word):
        permut = list(itertools.permutations(word))
        for li in permut:
            option = ""
            for variant in li:
                option += variant
            print(option)

    word = input("Enter the word: ")
    do_permutation(word)
    
#task 6
class Solution:
    def reverse_string(sentence):        
        reversed_sentence = reversed(sentence)
        answer = ' '.join(word for word in reversed_sentence)
        print(answer)

    sentence = input("Enter the sentence: ")
    sentence = sentence.split()
    reverse_string(sentence)

#task 7
class Solution:
    def has_33(nums):
        for i in range(len(nums)):
            if nums[i-1]==nums[i] and nums[i]==3:
                return True
        return False


    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    if has_33(nums):
        print("True")
    else:
        print("False")