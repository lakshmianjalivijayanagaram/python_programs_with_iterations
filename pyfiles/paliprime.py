def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
    return rev
      
def ispaliPrime(n):
    rev=reverse(n)
    if rev==n and isPrime(n):
        return True
    else:
        return False
def printPaliprime(ll,ul):
    for i in range(ll,ul+1):
        if ispaliPrime(i):
            print(i)
printPaliprime(1,100)
def printNPaliprime(count):
    c=0
    n=1
    while True:
        if ispaliPrime()
    
