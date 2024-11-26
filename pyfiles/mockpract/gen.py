'''def genfunction():
    print('genf is started')
    yield 25
    print('content of genf after yielding')
    yield 'hello'
    print('content of genf after yielding')
    print('last')
    yield 89,34,'bye'
gnf=genfunction()
print(gnf)
print(next(gnf))
print(next(gnf))
print(next(gnf))
print(next(gnf))'''
''''def rangegen(ll,ul,up=1):
    while ll<=ul:
        yield ll
        ll+=up
rgo=rangegen(1,10,2)
for i in rgo:
    print(i,end=" ")
def fibo(fv,sv,n):
    i=1
    while i<=n:
        yield fv
        fv,sv=sv,fv+sv
        i+=1
fioo=fibo(1,2,10)
for i in fioo:
    print(i)


def genfun(ll,ul,up):
    while ll<=ul:
        yield ll
        ll+=up
f1=genfun(1,10,2)
for i in f1:
    print(i,end=' ')

def fibo(fv,sv,n):
    i=1
    while i<=n:
        yield fv
        i+=1
        fv,sv=sv,fv+sv
fib=fibo(1,2,10)
for i in fib:
    print(i,end=' ')
def gen():
    i=1
    while i<2:
        yield i
        i+=1
go=gen()
print(go.__sizeof__())
print(iter([11]).__sizeof__())
'''







        



















