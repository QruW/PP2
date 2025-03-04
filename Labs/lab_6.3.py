import os

path = r'C:\Users\aibar\OneDrive\Рабочий стол\Вообщем и в целом\VSCode\Новая папка'

if os.access(path, os.F_OK):
    contents = os.listdir(path)
    path_1 = './'
    for element in contents:
        print(element)
        print(path_1)
else:
    print("This path is not exist")
    