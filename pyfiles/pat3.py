"""n=int(input())
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    stars+=1
 
n=int(input())
stars=n

for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if row%2!=1:
            dummy+=2
        else:
            dummy+=1
    print()
    stars-=1
  
    
  
"""
