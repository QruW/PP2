import re

with open('test.txt', 'r') as file:
    content = file.read()

def find_lowercase_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

print(find_lowercase_underscore(content))