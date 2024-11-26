'''
#1
n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
     
    print()
    stars+=1
    dummy+=1
#2
n=int(input())
stars=1
spaces=0
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
    
    print()
    spaces+=1
    dummy+=1
#3   
n=int(input())
stars=1
spaces=n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(dummy+64),end=" ")
    
    print()
    spaces-=1
    dummy+=1
#4
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print(chr(dummy+64),end=" ")
        else:
            print(" ",end=" ")

    print()
    dummy+=1
'''









