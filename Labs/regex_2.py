import re

with open('test.txt', 'r') as file:
    content = file.read()

def match_a_bb(s):
    return re.fullmatch(r'a(bb|bbb)', s) is not None

print(match_a_bb(content))