n=int(input())
stars=n
s=1
for row in range(1,n+1):
    
    dummy=s
    
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
        
    print()
    stars-=1
    s=s+5
