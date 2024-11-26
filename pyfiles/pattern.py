#n=int(input())
"""for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print("*",end=" ")
        else:
            print("@",end=" ")
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print("*",end=" ")
        else:
            print("@",end=" ")
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print("*",end=" ")
        else:
            print("A",end=" ")
    print()

for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print("*",end=" ")
        else:
            print("A",end=" ")
    print()

"""
n=int(input())
spaces=1
stars=n
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars-=2
    spaces+=1

        
    
"""
spaces=n-1
stars=1
 if row!=n:
        for sp in range(1,spaces+1):
            print(" ",end=" ")
        for st in range(1,stars+1):
            print("*",end=" ")
        print()
        stars+=2
        spaces-=1       
"""    



