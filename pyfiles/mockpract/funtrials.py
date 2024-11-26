'''def fun(*args):
    print(args)
    count=0
    for i in args:
        count+=1
    print(count)
fun(10,20,304,5,6)'''

'''def isEven(n):
    if n%2==0:
        return True
    else:
        return False

def printEven(ll,ul):
    for i in range(ll,ul+1):
        if isEven(i):
            print(i)
printEven(1,20)

def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
def primeRange(ll,ul):
    for i in range(ll,ul+1):
        if isprime(i):
            print(i)
primeRange(1,20)

def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def nprime(count):
    pc=0
    n=2
    while True:
        if isprime(n):
            print(n)
            pc+=1
            if pc==count:
                break
        n+=1
nprime(10)


def rev(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def paliprime(n):
    val=rev(n)
    if val==n and prime(n):
        return True
    else:
        return False
def paliprimerange(ll,ul):
    for i in range(ll,ul+1):
        if paliprime(i):
            print(i)
paliprimerange(1,100)

def rev(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def isemirp(n):
    val=rev(n)
    if prime(n) and prime(val) and val!=n:
        return True
    else:
        return False
def isemirprange(ll,ul):
    for i in range(ll,ul+1):
        if isemirp
        (i):
            print(i)
isemirprange(1,200)

def isdisarium(n):
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l=l-1
    if n==summ:
        return True
    else:
        return False
def rangedis(ll,ul):
    for i in range(ll,ul+1):
        if isdisarium(i):
            print(i)
#rangedis(1,200)
def nthdis(count):
    pc=0
    n=1
    while True:
        if isdisarium(n):
            print(n)
            pc+=1
            if pc==count:
                break
        n+=1
#nthdis(10)
def nthdis(count):
    pc=0
    n=1
    while True:
        if isdisarium(n):
            
            pc+=1
            if pc==count:
                print(n)
                break
        n+=1
nthdis(10)
'''
def special(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        summ+=fact
    if n==summ:
        return True
    else:
        return False
def specialrange(ll,ul):
    for i in range(ll,ul+1):
        if special(i):
            print(i)
#specialrange(1,200)
def nthsp(count):
    pc=0
    n=1
    while True:
        if special(n):
            pc+=1
            if pc==count:
                print(n)
                break
        n+=1
nthsp(3)
def ntthsp(count):
    pc=0
    n=1
    while True:
        if special(n):
            print(n)
            pc+=1
            if pc==count:
                break
        n+=1
ntthsp(3)






































        
