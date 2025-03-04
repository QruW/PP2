import re

with open('test.txt', 'r') as file:
    content = file.read()

def insert_spaces_capital(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(insert_spaces_capital(content))