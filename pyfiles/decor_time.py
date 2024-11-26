'''def timeDecor(arg):#arg=fibo function address
    def inner():
        import time
        it=time.time()
        arg()#fibo function address
        ft=time.time()
        print(ft-it)
    return inner
@timeDecor#fibo=timeDecor(fibo function address)#fibo=inner function adress
def fibo():
    fn=int(input())
    sn=int(input())
    n=int(input())
    if n==1:
        print(sn)
    elif n==2:
        print(fn)
    else:
        print(fn,sn)
        for i in range(n-2):
            tn=fn+sn
            print(tn)
            fn,sn=sn,tn
        
fibo()
@timeDecor
def prime():
    ll=int(input())
    ul=int(input())
    for n in range(ll,ul+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)

prime()

#Zero Division Error Solving
def dWoutError(arg):#division function address
    def inner(a,b):
        if b==0:
            arg(b,a)#divisin function address calling
        else:
            arg(a,b)#division function address calling
    return inner
@dWoutError#division=dWoutError(division function address)#division=inner function address
def division(a,b):
    print(a/b)
division(10,2)
division(10,0)
'''





















