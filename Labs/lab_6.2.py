import os 

path = r'C:\Users\aibar\OneDrive\Рабочий Стол\Вообщем и в целом'

# using relative path
print(os.access(path, os.F_OK)) # check for existence
print(os.access(path, os.R_OK)) # check for readibility
print(os.access(path, os.W_OK)) # check for writability
print(os.access(path, os.X_OK)) # check for executability