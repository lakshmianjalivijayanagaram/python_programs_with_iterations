'''n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()

n=int(input('enter the number'))
for i in range(1,n+1):
    print('* '*i)
n=int(input('enter the number'))
for i in range(1,n+1):
    print('* '*n)

n=int(input('enter the number'))
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()

n=int(input('enter the number'))
for row in range(1,n+1):
    for col in range(1,row+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input('enter the number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input('enter the number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1 or row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input('enter the number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input('enter the number'))
dummy=1
for row in range(1,n+1):
    for st in range(1,n+1):
        print(dummy,end=' ')
    print()
    dummy+=1

n=int(input('enter the number'))
for row in range(1,n+1):
    dummy=1
    for st in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()


n=int(input('enter the number'))
st=n
for row in range(1,n+1):
    dummy=1
    for i in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    st-=1

n=int(input('enter the number'))
sp=n-1
st=1
for row in range(1,n+1):
    dummy=n
    for i in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    n-=1
    st+=1
    sp-=1

n=int(input('enter the number'))
sp=0
st=n
for row in range(1,n+1):
    dummy=row
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for i in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    st-=1
    sp+=1

n=int(input('enter the number'))
dummy=1
for row in range(1,n+1):
    
    for i in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()




n=int(input('enter the number'))
dummy=1
st=n
for row in range(1,n+1):
    #a=n
    #dummy=n
    for st in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    dummy+=row-1
    st-=1
    

n=int(input('enter the number'))
dummy=5
st=1
sp=n-1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    dummy+=n-(row+1)
    st+=1
    sp-=1

n=int(input('enter the number'))
dummy=1
st=1
#sp=n-1
for row in range(1,n+1):
    for st in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    dummy+=n-row
    st+=1


n=int(input('enter the number'))
dummy=5
st=1
sp=n-1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    dummy+=n-(row+1)
    st+=1
    sp-=1

n=int(input('enter num'))
for row in range(1,n+1):
    dummy=row
    for i in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()

n=int(input('enter num'))
st=n
sp=1
dummy=1
for row in range(1,n+1):
    #dummy=row+1
    for sp in range(1,sp+1):
        print(' ',end=' ' )
    for i in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    st-=1
    sp+=1
    a=3
    dummy-=a
    a-=1

n=int(input('enter num'))
st=1
sp=n-1

for row in range(1,n+1):
    dummy=5
    for sp in range(1,sp+1):
        print(' ',end=' ' )
    for i in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    st+=1
    sp-=1


n=int(input('enter num'))
st=n
sp=1
dummy=1
for row in range(1,n+1):
    a=1
    dummy=a
    for sp in range(1,sp+1):
        print(' ',end=' ' )
    for i in range(1,st+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    st-=1
    sp+=1
    a+=2

n=int(input('enter num'))
st=n
for row in range(1,n+1):
    dummy=row
    for st in range(1,st+1):
        print(dummy,end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
        
    print()
    st-=1


n = 5
spaces = 0
for st in range(1, 2*n-1, 2):
    for sp in range(spaces):
        print(' ', end=' ')
        for en in range(n+1, 2*n+1):
            for num in range(st, en):
                print(num, end=' ')
        print()
        spaces += 1

n=int(input('enter the num'))
for row in range(1,n+1):
    if row%2==1:
        dummy=1
    else:
        dummy=6
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()

st=1
n=int(input('enter the num'))
for row in range(1,n+1):
    if row%2==1:
        dummy=1
    else:
        dummy=6
    for col in range(1,st+1):
        print(dummy,end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    st+=1
'''










        















        
        













                  
