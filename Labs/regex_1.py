import re

with open('test.txt', 'r') as file:
    content = file.read()

def match_a_b(s):
    return re.fullmatch(r'a*b*', s) is not None

print(match_a_b(content))