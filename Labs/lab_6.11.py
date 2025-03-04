import string

str = "AppiA"

str1 = ''.join(reversed(str))

if str == str1:
    print("It is a polindrome")
else:
    print("It is not a polindrome")
