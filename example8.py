'''class A:
    def __init__(self,a):
        self.a=a
        print('base class')

    def fun(self):
        print(self.a)

class B(A):
    def __init__(self,a):
        self.a=a
        super().__init__(a)
        print('derived class B')

    def fun(self):
        print(self.a)

class C(B):
    def __init__(self,a):
        self.a=a
        super().__init__(a)
        print('derived class C')

    def fun(self):
        print(self.a+' in class C')

obj = B('Hi')
obj.fun()
'''
count = 0
max = 0
l = [0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1]
'''for i in l:
    if i == 1:
        count+=1
        if count>max:
            max = count
    else:
        count = 0

print(max)
'''

