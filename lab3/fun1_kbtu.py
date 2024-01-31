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

#task 8
class Solution:
    def spy_game(nums):
        for i in range(2, len(nums)):
            if nums[i-2]==0 and nums[i-1]==0 and nums[i]==7:
                return True

    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    if spy_game(nums):
        print("True")
    else:
        print("False")

#task 9
import math
class Solution:
    def find_volume(r):
        volume = 4/3 * math.pi * r**3
        print(volume)

    r = input("Enter the radius: ")
    r = int(r)
    find_volume(r)

#task 10
class Solution:
    def unique(nums):
        nums.sort()
        prev = nums[0]
        ans = [prev]
        for i in range(len(nums)):
            if prev != nums[i]:
                ans.append(nums[i])
                prev = nums[i]

        print(ans)


    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    unique(nums)

#task 11
class Solution:
    def is_palindrome(phrase):
        return phrase == phrase[::-1]

    phrase = input("Enter the phrase: ")
    if is_palindrome(phrase):
        print("it is palindrome")
    else:
        print("it is not palindrome")

#task 12
class Solution:
    def histogram(nums):
        for num in nums:
            print('*'*num)
    
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    histogram(nums)

from random import randrange
class Solution:
    def guessr():
        name = input("Hello! What is your name? ")
        count = 1
        print("Well, {}, I am thinking of a number between 1 and 20".format(name))
        target = randrange(1, 20)
        guess = input("Take a guess ")
        guess = int(guess)

        while guess != target:
            if guess < target:
                print("Your guess is too low.")
                guess = int(input("Take a guess."))
            elif guess > target:
                print("Your guess is too high.")
                guess = int(input("Take a guess."))
            else:
                break
            count += 1
        print("Good job, {}! You guessed my number in {} guesses!".format(name, count))
    guessr()