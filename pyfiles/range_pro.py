"""
#perfect num :1 to 10
count=int(input())
pc=0
n=1
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
    n=n+1

#perfect count-10th only
        
count=int(input())
pc=0
n=1
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
    n=n+1

#perfect count-5th to 10th 

pc=0
n=1
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        pc+=1
        if pc>=2 and pc<=5:
            print(n)
        if pc==5:
            break
    n=n+1

#niven number-first 10
count=int(input())
n=1
hc=0
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        print(n)
        hc+=1
    if hc==count:
        break
    n+=1
        

#niven-only 10
count=int(input())
n=1
hc=0
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        hc+=1
        if hc==count:
            print(n)
            break
    n+=1
    

#niven-5th to 10th
count1=int(input())
count2=int(input())
n=1
hc=0
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem
    if n%summ==0:
        hc+=1
        if hc>=count1 and hc<=count2:
            print(n)
        if hc==count2:
            break
    n+=1


#arm-upto 10
count=int(input())
ac=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        print(n)
        ac+=1
        if ac==count:
            break
        
        
    n+=1

#armstrong-only 10
count=int(input())
ac=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        ac+=1
        if ac==count:
            print(n)
            break
    n+=1

#armstrong-1 to 10
count1=int(input())
count2=int(input())
ac=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        ac+=1
        if ac>=count1 and ac<=count2:
            print(n)
        if ac==count2:
            break
    n+=1


#disarium-upto10
count=int(input())
dc=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l=l-1
    if summ==n:
        print(n)
        dc+=1
        if dc==count:
            break
    n+=1

#disarium-only10
count=int(input())
dc=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l=l-1
    if summ==n:
        dc+=1
        if dc==count:
            print(n)
            break
    n+=1

#disarium-1 to 10
count1=int(input())
count2=int(input())
dc=0
n=1
while True:
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l=l-1
    if summ==n:
        dc+=1
        if dc>=count1 and dc<=count2:
            print(n)
        if dc==count2:
            break
    n+=1

"""




    
    
