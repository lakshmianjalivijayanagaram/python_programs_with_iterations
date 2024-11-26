'''s='Bye'
count=0
for i in s:
    print(i)
    count+=1
print(count)

ms=input('enter mainstring')
ss=input('enter substring')
count=0
for i in ms:
    if i==ss:
       count+=1
print(count)

a='123anja87'
count=0
for i in a:
    if i.isdigit():
        count+=int(i)
print(count)

a='123anja87'
odd=0
even=0
for i in a:
    if i.isdigit():
        if int(i)%2==0:
            even+=int(i)
        else:
            odd+=int(i)
        
print(abs(even-odd))

a='anja@#$li7927'
vo='aeiouAEIOU'
count=0
for i in a:
    if not i.isalnum():
        
            count+=1
print(count)
li=[1,2,3,1,2,'anjali']
summ=0
for i in li:
    if isinstance(i,int):
        summ+=i
print(summ)

a=[1,4,9,0,2]
max=a[0]
for i in a:
    if i>max:
        max=i
print(i)


a=eval(input())
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
a=eval(input())
d={}
for i in a:
    d[i]=a.count(i)
print(d)

a=eval(input())
d={}.fromkeys(a,0)
for i in a:
    d[i]+=1
print(d)

s='hai hello how ae yoyu anjali hai'
a=s.split()
c=0
mxww=''
for i in a:
    if len(i)>c:
        c=len(i)
        mxww=i
print(mxww)

a=int(input())
b=int(input())
for i in range(a,b):
    if i%2==0:
        print(i)

a=int(input())
b=int(input())
summ=0
for i in range(a,b+1):
    summ+=i
print(summ)

n=int(input())
summ=0
for i in range(1,n+1):
    summ+=i
print(summ)
n=int(input('enter the number'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

n=int(input())
summ=0
for i in range(1,n//2+1):
    if n%i==0:
        summ+=i
if n==summ:
    print('perfect number')
else:
    print('not a perfect number')

s=input()
for i in range(0,len(s)):
    if s[i]=='h':
        print(i)

s=input()
for i in range(0,len(s)):
    if i in '02468':
        print(s[i])

s=input()
for i in range(0,len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i)


s=input()
new=''
for i in range(0,len(s)):
    if s[i] in 'AEIOUaeiou':
        new+=str(i)
    else:
        new+=s[i]
print(new)



s=input()
summ=0
for i in range(1,len(s),2):
    if s[i] in '02468':
        summ+=int(s[i])
print(summ)

s='anjali'
rev=''
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)

s='anjali'
rev=''
for i in s:
    rev=i+rev
print(rev)
'''
a=[10,11,12,13,14,15]
for i in range(len(a)//2):
    a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
print(a)

    








        
