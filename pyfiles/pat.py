n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=" ")
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    
#n=int(input())
space=0
stars=n
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    space+=1
    stars-=1
    dummy+=1
  

#n=int(input())
spaces=0
stars=n
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    spaces+=1
    stars-=1

#n=int(input())
spaces=n-1
stars=1

for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    spaces-=1
    stars+=2
    dummy+=1
   

#n=int(input())
spaces=n//2
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
    dummy+=1

#n=int(input())
spaces=0
stars=2*n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    spaces+=1
    stars-=2
    dummy+=1




#n=int(input())
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    spaces+=1
    dummy+=1
    
#n=int(input())
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
    print()
    spaces-=1
    dummy+=1



#n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(' ',end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    spaces-=1
    stars+=1
    n=n-1






    
