file_name = 'info.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)
a = 0

with open(file_name, 'r') as file: 
    for line in file:
        print(file.readline())
        if file.readline():
            a = a + 1

with open(file_name, 'r') as file: 
    for element in file:
        print(file.readline())
        if file.readline():
            a = a + 1
    
print(a)