n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect")
else:
    print("not perfect")





"""a=int(input())
b=int(input())
sum=0
for i in range(a,b+1):
    sum=sum+i
print(sum)

n=int(input())
sum=0
for i in range(n):
    sum=sum+i
print(sum)

n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
"""
