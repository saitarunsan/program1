class A:
    a = 10
    def __init__(self):
        print('this is constructor')

    def printer(self):
        print('this is instance method')

    @classmethod
    def getter(cls):
        print('a=',cls.a)

    @staticmethod
    def checker():
            print('hey im staticmethod')

obj = A()
obj.getter()
obj.checker()