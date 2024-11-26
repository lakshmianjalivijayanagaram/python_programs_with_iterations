car=[12,13,11,4,5,19,2,8,7,12,5]
fine=[10,10,20,17,15,12,13,9,1,3,1]
a=list(zip(car,fine))
print(a)
a=dict(zip(car,fine))
print(a)





'''fn=0
sn=1
for i in range(14-1):
    tn=fn+sn
    fn,sn=sn,tn
print(tn)





a=['hello','helloworld','hell','helo']
mlen=9999999
lenw=''
for i in a:
    if len(i)<mlen:
        mlen=len(i)
        lenw=i
print(lenw)
maxlen=0
maxlenw=''
for i in a:
    if len(i)<maxlen:
        maxlen=len(i)
        maxlenw=''
compre=''
word=''
for i in range(0,mlen):
    word+=lenw[i]
for i in range(0,len(lenw)):
    if lenw[i]==word[i]:
        compre=compre+lenw[i]
print(compre)
    



arr=[1,2,3,4,5]
k=4
a=[]
for i in range(len(arr)-1,-1,-1):
    if k in arr:
        b=arr.index(arr[i])
        a.append(b)
print(a)
if len(a)>=1:
    print(max(a))
else:
    print(-1)





S="Pack mY box witH fIve dozen liquor jugs"
a='abcdefghijklmnopqrst'
S.sorted()
print(S)
b=S.lower().replace(' ','')
print(b)

if a==c:
    print(1)
else:
    print(0)

def pattern(n):
    if n>0:
        return n+5
    elif n<0:
        return n-5
    else:
        return 0
    return n,pattern(n)
print(pattern(16))

'''



































'''def single(nums):
    for i in nums:
        if nums.count(i)==1:
            return i
print(single([2,2,1]))    












a='anjallGJGi'
a=a.lower()
print(a)
s='anjali 12 ANJN'
p=''
for i in s:
    if i.isalnum():
        p=p+i
print(p.lower())












nums=[4,1,2,1,2]
a={}
for i in nums:
   a[i]=nums.count(i)
print(a)
for i in a:
   if a[i]==1:
     print(i)














n=int(input())
stars=1
spaces=n
for row in range(1,n+1):
   dummy=1
   for sp in range(1,spaces+1):
      print("",end=" ")
   for st in range(1,spaces+1):
      if row=1:
         print(dummy,end=" ")
      elif row=2:
         print(dummy,

l=[1,2,3]
a=''
for i in l:
   a=a+'i'
print(a)
nums=[11,22,33,44,55]
target=66
for i in range(len(nums)):
   if target-nums[i] in nums:
        
        print(i,nums.index(target-nums[i]))
        break
    '''
