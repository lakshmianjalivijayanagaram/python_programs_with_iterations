'''
ll=int(input('enter the number'))
ul=int(input('enter the number'))
for n in range(ll,ul+1):
    subs=0
    for i in range(1,n//2+1):
        if n%i==0:
            subs+=i
    if subs==n:
        print(n)
            

#ll=int(input('enter the number'))
#ul=int(input('enter the number'))
def prime(ll,ul):
    for n in range(ll,ul+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                return n
        
        
print(prime(1,100))
ll=int(input('enter the number'))
ul=int(input('enter the number'))
for n in range(ll,ul+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                 print(n)


ll=int(input('enter the number'))
ul=int(input('enter the number'))
for n in range(ll,ul+1):
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        print(n)


ll=int(input('enter the number'))
ul=int(input('enter the number'))
for n in range(ll,ul+1):
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l-=1
    if summ==n:
        print(n)



ll=int(input('enter the number'))
ul=int(input('enter the number'))
for n in range(ll,ul+1):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        print(n)

l=[]
while True:
    
    val=int(input())
    if val%2==0:
        l.append(val)
    else:
        break
print(l)

pc=0
#c=int(input('enter num'))
n=1
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
            if pc==10:
                break
    n+=1

count=int(input())
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc==count:
                print(n)
                break
                
    n+=1


n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc>=5 and pc<=10:
                print(n)
            else:
                if pc>10:
                    break
    n+=1


n=1
pc=0
n=1
while True:
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        print(n)
        pc+=1
        if pc==10:
            break
    n+=1


n=1
pc=0
n=1
while True:
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        pc+=1
        if pc>=5 and pc<=10:
            print(n)
        else:
            if pc>10:
               break
    n+=1

pc=0
n=1
count=int(input('enter the num'))
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        print(n)
        pc+=1
        if pc==count:
            break
    n+=1


pc=0
n=1
count=int(input('enter the num'))
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        pc+=1
        if pc>=1 and pc<=4:
            print(n)
            
        else:
            if pc>4:
               break
    n+=1

pc=0
n=1
count=int(input('enter the num'))
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        pc+=1
        if pc==count:
            print(n)
            break
    n+=1


pc=0
count=int(input())
n=1
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        print(n)
        pc+=1
        if pc==count:
            break
    n+=1



pc=0
count=int(input())
n=1
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        #print(n)
        pc+=1
        if pc>=5 and pc<=10:
            print(n)
        else:
            if pc>10:
                break
    n+=1


pc=0
count=int(input('enter  num'))
n=1
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        summ+=fact
        
    if summ==n:
        print(n)
        pc+=1
        if pc==count:
            break
    n+=1

spaces=0
stars=1
n=int(input('entern numm'))
for row in range(1,n+1):
    for i in range(1,spaces+1):
        print(' ',end=' ')
    for j in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1

n=int(input('entern numm'))
spaces=n-1
stars=1
for row in range(1,n+1):
                                   for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1

n=int(input('entern numm'))
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
       print('*',end=' ')
    print()
    stars+=1

n=int(input('entern numm'))
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1
    spaces-=1

n=int(input('entern numm'))
spaces=0
stars=n
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
    spaces+=1

n=int(input('entern numm'))
stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1


n=int(input('entern numm'))
stars=1
spaces=2*n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1
'''
n=int(input('enter num'))
spaces=n//2
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
            
    

































































        


































        
    




















        















        












































    
















                 
