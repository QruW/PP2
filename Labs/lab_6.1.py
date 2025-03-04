import os

path = os.getcwd()
print(path)
print("-------------")

contents = os.listdir(path)

for element in contents:
    print(element)
    print(path)

print("-------------")

path2 = r'C:\Users\aibar\OneDrive\Рабочий стол\Вообщем и в целом'

contents1 = os.listdir(path2)

for element1 in contents1:
    print(element1)