import string

str = "Ancient Apparatus"

u = 0
l = 0

for chr in str:
    if chr >= 'A' and chr <= 'Z':
        u = u + 1
    elif chr >= 'a' and chr <= 'z':
        l = l + 1

print(u)
print(l)