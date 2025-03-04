a = True
b = True
c = False
d = tuple([a,b,c])

if all(d) == True:
    print("all elements are True")
else:
    print("there are False elements")