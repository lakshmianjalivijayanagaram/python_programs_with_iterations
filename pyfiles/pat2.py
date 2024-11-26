n=int(input())
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1
  
n=int(input())
stars=n
spaces=0
dummy=1
for row in range(1,n+1):
    
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars-=1
    spaces+=1
    dummy=dummy-

n=int(input())
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars-=1
    
n=int(input())
stars=1
spaces=n-1

for row in range(1,n+1):
    dummy=n
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1
    spaces-=1
