n=145
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    summ+=fact
print(summ==n)
"""if(summ==n):
    print('strong num')
else:
    print('not strong num')
"""
 
