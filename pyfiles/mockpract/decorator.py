'''def brother(arg):
    def inner():
        print('brother started monitoring')
        arg()
        print('brother ended monitoring')
    return inner
@brother
def sister():
    print('sister started talking')
    print('sisiter ended talking')
#print(sister)
sister()
def timeDecor(arg):
    
    def inner():
        import time
        it=time.time()
        arg()
        ft=time.time()
        print(ft-it)
    return inner
@timeDecor

def fibo():
    fn=int(input())
    sn=int(input())
    n=int(input())
    if n==1:
        print(fn)
    elif n==2:
        print(fn,sn)
    else:
        print(fn,sn)
        for i in range(0,n-2):
            tn=fn+sn
            print(tn)
            fn,sn=sn,tn
fibo()
@timeDecor
def prime():
    ll=int(input())
    up=int(input())
    for n in range(ll,up+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)
prime()

@timeDecor
'''
def dWError(arg):
    def inner(a,b):
        if b==0:
            arg(b,a)
        else:
            arg(a,b)
    return inner
@dWError
def division(a,b):
    print(a/b)
division(0,11)













            
        

                   
