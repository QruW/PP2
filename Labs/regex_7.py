import re

with open('test.txt', 'r') as file:
    content = file.read()

def snake_to_camel(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))

print(snake_to_camel(content))