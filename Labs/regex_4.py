import re

with open('test.txt', 'r') as file:
    content = file.read()

def find_upper_lower(s):
    return re.findall(r'\b[A-Z][a-z]+\b', s)

print(find_upper_lower(content))