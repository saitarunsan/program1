a = 10
print(id(a))

b = 50
#print(id(b))

c = a
print(id(c))



def sum(x):
    print(x)
    print(id(x))
    x = x+1
    print(x)
    print(id(x))

sum(c)
print(c)
