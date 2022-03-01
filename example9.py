'''
def login_required(f1):
    def inner(name,is_login):
        if is_login==False:
            print('please do login.')
            return
        f1(name,is_login)
    return inner

@login_required
def home(name,is_login):
    print('welcome back buddy!')

@login_required
def orders(name,is_login):
    print('migrating to orders.....')


def about():
    print('we are very happy to share about us.')

home('sai tarun',True)
orders('sai tarun',False)
about()
'''

'''
def checker(f1):
    def inner(a,b):
        if b==0:
            print('enter valid divisor')
        elif b>a:
            a,b = b,a
        f1(a,b)
    return inner

@checker
def divd(a,b):
    print(a/b)
divd(14,7)'''
