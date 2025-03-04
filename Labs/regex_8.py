import re

with open('test.txt', 'r') as file:
    content = file.read()

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

print(split_at_uppercase(content))