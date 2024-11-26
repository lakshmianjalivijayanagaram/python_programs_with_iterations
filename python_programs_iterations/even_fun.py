'''#write even numbers using function:
def isEven(n):
    if n%2==0:
        return 'a is even'
    else:
        return 'a is odd'
def printEvenNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isEven(i):
            print(i)
printEvenNumbers(1,10)


#write prime numbers in a range
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
def printPrime(ll,ul):
    for i in range(ll,ul+1):
        if isPrime(i):
            print(i)
printPrime(1,100)
#for first n primes'
def printnPrime(count):
    pc=0
    n=2
    while True:
        if isPrime(n):
            print(n)
            pc+=1
            if pc==count:
                break
        n+=1
printnPrime(10)

#for armstrong numbers

def isArmstr(n):
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if n==summ:
        return True
    else:
        return False
#armstrong numbers in a range
def printArmstr(ll,ul):
    for i in range(ll+ul+1):
        if isArmstr(i):
            print(i)
printArmstr(1,1000)

#first n armstrong numbers

def printnArmstr(count):
    ac=0
    n=1
    while True:
        if isArmstr(n):
            print(n)
            ac+=1
            if ac==count:
                break
        n+=1
printnArmstr(10)

#print disarium numbers


def isDisarium(n):
    summ=0
    dummy=n
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
def printDisarium(count):
    dc=0
    n=1
    if isDisarium(n)      



    
        









        
