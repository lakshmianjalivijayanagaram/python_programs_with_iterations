'''#n=int(input('enter number'))
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
ll=int(input('enter the number'))
up=int(input('enter the number'))
def print_even(ll,up):
    for i in range(ll,up+1):
        if iseven(i):
            print(i)
print_even(ll,up)

def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def prime_range(ll,up):
    for i in range(ll,up+1):
        if isprime(i):
            print(i)
prime_range(2,20)
def prime_range(count1,count2):
    c=0
    n=2
    while True:
        if isprime(n):
            print(n)
            c+=1
            if c>=count1 and c<=count2:
                break
        n+=1
prime_range(5,10)'''

'''
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
def ispaliprime(n):
    re=reverse(n)
    if n==re  and isprime(n):
        return True
    else:
        return False
def pali_range(ll,up):
    for i in range(ll,up+1):
        if ispaliprime(i):
            print(i)
pali_range(1,150)



def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
def ispaliprime(n):
    if reverse(n)==n and isprime(n):
        return True
    else:
        return False
def printt(count):
    c=0
    n=1
    while True:
        if ispaliprime(n):
            print(n)
            c+=1
            if c==count:
                break
        n+=1
            
printt(10)

def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
def emirp(n):
    rev=reverse(n)
    if rev!=n and isprime(rev) and isprime(n):
        return True
    else:
        return False
def range(c):
    count=0
    n=1
    while True:
        if emirp(n):
            print(n)
            count+=1
            if c==count:
                break
        n+=1
range(10)



l=eval(input())
print(l)
print(type(l))

n=int(input('enter the number'))
stars=n
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1


num = 5
spaces = 0
for line in range(num+1, 1, -1):
    for sp in range(spaces):
        print(' ', end=' ')
    for st in range(1, line):
        print(st, end= ' ')
    print()
    
    spaces += 1


n=int(input('enter the number'))
stars=2*n-1
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=2
    spaces+=1'''

num = 5
spaces = 0
for line in range(num*2, 1, -2):
    for sp in range(spaces):
        print(' ', end = ' ')
    for st in range(1, line):
        print(st, end= ' ')
    print()
    spaces += 1




















'''def sum(a,b):
    print(a+b)
sum(10,20)
print(sum)
def sum():
    if 10>5:
        return 10
    else:
        return 5
print(sum())

def sum(a,b):
    if a>b:
        return a,b
    else:
        return b
print(sum(50,20))
def fun(*args):
    print(args)
    print(type(args))
fun(10,20,30,40,50,60)
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(a=10,b=20,c=30,d=30)'''
