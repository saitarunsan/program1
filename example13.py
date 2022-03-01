import copy
from copy import deepcopy
'''a = 10
b = 2
a=b
print('a-id',id(a))
print('b-id',id(b))
print(a)
print(b)'''
"""
a = [1,2,3,4,[6,7,8]]
'''b = copy.copy(a)
print('b:',b)
print('b-id',id(b))
print('b inner list-id',id(b[4]))
print('a inner list-id',id(a[4]))
a.append(5)
a[4].append(9)
print(a)
print(b)
'''

b = copy.deepcopy(a)
print('a:',a)
print('b:',b)
print('a-id',id(a))
print('b-id',id(b))
print('a inner list-id',id(a[4]))
print('b inner list-id',id(b[4]))
a[4].append(9)
a.append(5)
print('a:',a)
print('b:',b)
"""