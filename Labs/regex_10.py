import re

with open('test.txt', 'r') as file:
    content = file.read()

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

print(camel_to_snake(content))