'''n=int(input())
stars=1
spaces=n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
    print()
    stars+=2
    spaces-=1
    dummy+=1

n=int(input())
stars=1
spaces=n//2
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1
    dummy+=1

n=int(input())
spaces=0
stars=2*n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
    print()
    spaces+=1
    stars-=2
    dummy+=1
'''
        
