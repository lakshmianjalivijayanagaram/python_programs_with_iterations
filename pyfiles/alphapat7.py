'''n=int(input())
stars=n
dummy=1
for row in range(1,n+1):
    
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    stars-=1
'''
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
        if row%2==1:
            dummy+=1
        else:
            dummy+=2

    print()
    stars+=1
    spaces-=1
'''
n=int(input())
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()
    stars+=1

n=int(input())
stars=n
spaces=0
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
        if row%2==1:
            dummy+=1
        else:
            dummy+=2

    print()
    stars-=1
    spaces+=1
'''







