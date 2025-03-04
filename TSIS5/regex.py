import re

def match_a_b(s):
    return bool(re.fullmatch(r'a*b*', s))

def match_a_b_limited(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

def find_lowercase_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

def find_upper_lower_sequence(s):
    return re.findall(r'[A-Z][a-z]+', s)

def match_a_anything_b(s):
    return bool(re.fullmatch(r'a.*b', s))

def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

def snake_to_camel(s):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(s.split('_')))

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

def insert_spaces_at_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

# Example usage:
print(match_a_b("ab"))  # True
print(match_a_b_limited("abb"))  # True
print(find_lowercase_underscore("this_is_a_test another_example"))
print(find_upper_lower_sequence("HelloWorld PythonRegex"))
print(match_a_anything_b("a123b"))  # True
print(replace_with_colon("Hello, world. How are you?"))
print(snake_to_camel("this_is_a_test"))  # ThisIsATest
print(split_at_uppercase("HelloWorld"))
print(insert_spaces_at_capitals("HelloWorldTest"))
print(camel_to_snake("CamelCaseString"))  # camel_case_string