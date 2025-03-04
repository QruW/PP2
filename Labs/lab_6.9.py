a = True
b = True
c = True
f = 0
d = tuple([a,b,c])
for element in d:
    while element == True:
        f = f + 1
if f == len(d):
    print("all elements are True")
else:
    print("there are False elements")