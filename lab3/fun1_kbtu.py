#task1

def to_ounces():
    grams = input("enter mass in grams: ")
    grams = int(grams)
    ounces = 28.3495231 * grams
    print(ounces)

#task2
def Fahrenheit_to_Celsius():
    F = input("Enter temperature in Fahrenheit: ")
    F = int(F)
    C = (5 / 9) * (F - 32)
    print(C)


#task3
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

#task4
def filter_prime():
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
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



#task 5
def do_permutation():
    import itertools
    word = input("Enter the word: ")
    permut = list(itertools.permutations(word))
    for li in permut:
        option = ""
        for variant in li:
            option += variant
        print(option)

#task 6
def reverse_string():        
    sentence = input("Enter the sentence: ")
    sentence = sentence.split()
    reversed_sentence = reversed(sentence)
    answer = ' '.join(word for word in reversed_sentence)
    print(answer)



#task 7
def has_33():

    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    ans = False

    for i in range(len(nums)):
        if nums[i-1]==nums[i] and nums[i]==3:
            ans = True

    if ans:
        print("True")
    else:
        print("False")

#task 8
def spy_game():
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    for i in range(2, len(nums)):
        ans = False
        if nums[i-2]==0 and nums[i-1]==0 and nums[i]==7:
            ans = True

        if ans:
            print("True")
        else:
            print("False")

#task 9
def find_volume():
    import math
    r = input("Enter the radius: ")
    r = int(r)
    volume = 4/3 * math.pi * r**3
    print(volume)

#task 10
def unique():
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    nums.sort()
    prev = nums[0]
    ans = [prev]
    for i in range(len(nums)):
        if prev != nums[i]:
            ans.append(nums[i])
            prev = nums[i]

    print(ans)

#task 11
def is_palindrome():
    phrase = input("Enter the phrase: ")
    if phrase == phrase[::-1]:
        print("it is palindrome")
    else:
        print("it is not palindrome")

#task 12
def histogram():
    input_numbers = input("Enter numbers separated by spaces: ")
    number_strings = input_numbers.split()
    nums = [int(num) for num in number_strings]
    histogram(nums)
    for num in nums:
        print('*'*num)


def guessr():
    from random import randrange
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