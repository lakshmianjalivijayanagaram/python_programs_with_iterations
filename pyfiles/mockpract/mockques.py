'''st='aaaabbbcc'
mainst=''
val=''
for i in st:
    if val=='' or val[-1]==i:
        val+=i
    else:
        mainst+=val[-1]
        mainst+=str(len(val))
        val=i

mainst+=val[-1]
mainst+=str(len(val))
print(mainst)

n=int(input())
st=1
spaces=n-1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print(dummy,end=' ')
        if st<=row-1:
            dummy+=2
        else:
            dummy-=2
    print()
    spaces-=1
    st+=2
'''


def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
def iscorrect(l):
    val=[]
    for i in range(1,len(l)):
        if 
        





























