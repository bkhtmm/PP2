# 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# 2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# 3
def solve(numheads, numlegs):

    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

# 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 5
import itertools

def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# 6
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

# 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
import math
def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0
    for num in nums:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False

#9
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

#10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

#11
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

#12
def histogram(lst):
    for value in lst:
        print('*' * value)

#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
