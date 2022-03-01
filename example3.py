a = 12
print(id(a))
#In call_by_value we gonna pass immutable datetypes as an arguments in the function and the changes made
#inside the function will not be reflected out the function.
def fun(b):
    print(b)
    print(id(b))
    b = b+1
    print(b)
    print(id(b))
fun(a)
print(id(a))


'''
a = [20]
print(a)
print(id(a))
#In call_by_reference we will be passing mutable datatypes where the changes
# made inside the function will also be reflected outside the function
def fun(b):
    print(b)
    print(id(b))
    b.append(30)
    print(b)
    print(id(b))
fun(a)
'''







