import re

with open('test.txt', 'r') as file:
    content = file.read()

def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

print(replace_with_colon(content))