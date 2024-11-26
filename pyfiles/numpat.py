n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if st<row:
            dummy+=1
        else:
           dummy-=1
    print()
    stars+=2
    spaces-=1
