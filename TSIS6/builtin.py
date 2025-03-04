from functools import reduce
import time
import math

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def count_case(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return upper, lower

def is_palindrome(string):
    return string == string[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

def all_true(tup):
    return all(tup)

# Example Usage
print(multiply_list([1, 2, 3, 4]))  # Output: 24

upper, lower = count_case("Hello World")
print("Upper case letters:", upper, "Lower case letters:", lower)  # Output: Upper case letters: 2 Lower case letters: 8

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

num, delay = 25100, 2123
print(f"Square root of {num} after {delay} milliseconds is", delayed_sqrt(num, delay))

print(all_true((True, True, True)))  # Output: True
print(all_true((True, False, True)))  # Output: False
