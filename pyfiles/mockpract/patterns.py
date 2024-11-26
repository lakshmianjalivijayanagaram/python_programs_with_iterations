#SELECT DISTINCT CITY FROM STATION
WHERE SUBSTR(CITY,1,1) IN ('A','E','I','O','U');
#generic approach
'''n=int(input('enter a number'))
stars=1
spces=n-1
for row in range(1,n+1):
    for sp in range(1,spces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('#',end=' ')
    print()
    stars+=2
    spces-=1
''' 
'''   
        # 
      # # # 
    # # # # # 
  # # # # # # # 
# # # # # # # # # 
'''
'''
n=int(input('enter a number'))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('!',end=' ')
    print()
    stars+=2
    spaces-=1

n=int(input('enter a number'))
stars=2*n-1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print('',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=2
    spaces+=2

n=int(input('enter a number'))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('1',end=' ')
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1

#1
n=int(input())
spaces=n-1
dummy=n
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    spaces-=1
    dummy-=row+1
    
#2
n=int(input())
stars=n
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=1

n=int(input())
stars=n
spaces=0
dummy=1
for row in range(1,n+1):
    
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    #dummy+=1
    stars-=1
    spaces+=1

n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
    print()
    dummy+=1

n=int(input('enter number'))

for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()

n=int(input('enter number'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()

n=int(input('enter number'))
dummy=1
stars=n
for row in range(1,n+1):
    for col in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    dummy+=row-1
    stars-=1


n=int(input('enter number'))
dummy=1
stars=n
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1
    dummy+=row

n=int(input('enter number'))
dummy=n
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars+=1
    spaces-=1
    dummy+=n-row-1

n=int(input('enter number'))
dummy=1
stars=1
#spaces=n-1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars+=1
    dummy+=n-row

n=int(input('enter number'))
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()

n=int(input('enter number'))
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=1

n=int(input('enter number'))
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars+=1
  
n=int(input('enter number'))
stars=n
spaces=0
dummy=1
a=3
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars-=1
    spaces+=1
    dummy-=a
    a-=1
n=int(input('enter number'))
stars=2*n-1
spaces=0

for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    spaces+=1
    stars-=2

  
n=int(input('enter number'))
stars=1
spaces=n
for row in range(1,n+1):
    dummy=5
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    stars+=1
    spaces-=1
 
n=int(input('enter number'))
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    

n=int(input('enter number'))
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    stars+=1


n=int(input('enter number'))
stars=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    stars-=1

n=int(input('enter number'))
stars=1
for row in range(1,n+1):
    dummy=row
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
    stars+=1
'''
n=int(input('enter number'))
stars=n

for row in range(1,n+1):
    if row%2==1:
        dummy=1
    else:
        dummy=n+1
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    


























'''n=int(input('enter the number'))
spaces=0
stars=1

for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for stas in range(1,stars+1):
        print("*",end='')
    print()
    spaces+=1

n=int(input('enter the number'))
def pat(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            if row>=col:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
pat(n)



n=int(input('enter the number'))
def pat(n):
    for i in range(1,n+1):
        for col in range(1,n+1):
            print('*',end=" ")
        print()
pat(n)

n=int(input('enter the number'))
for i in range(0,n):
    print('#'*n)
'''
