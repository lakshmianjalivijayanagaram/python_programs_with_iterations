n=int(input())
stars=n
dummy=1
for row in range(1,n+1):
    
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars-=1
    dummy=(dummy+row)-1

n=int(input())
stars=1
spaces=n-1
dummy=5
for row in range(1,n+1):
    
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1
    spaces-=1
    dummy=dummy+spaces
 
n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1
    dummy=dummy+n-1
    n=n-1

n=int(input())
stars=n
spaces=0
dummy=1
for row in range(1,n+1):
    dummy=dummy+row-1
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars-=1
    spaces+=1 
















    
