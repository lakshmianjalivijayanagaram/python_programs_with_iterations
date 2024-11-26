#print perfect numbers 1st to 5th
#6,28,496
n=1
pc=0
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        pc+=1
        if pc>=1 and pc<=5:
            print(n)
        if pc==5:
            break
    n=n+1
    
#PROCESS
'''
1.taking count as input to give upto how many HARSHAD numbers you want
2.checking from number 1 so taking n=1
3.taking initially harshadnumber count as 0 i.e hc=0
3.taking infinite loop because we dont know upto which number  'n' harshadnumbers  we get.
4.TAKINg SUM AS 0
5.checking for the divisrors in th range of the numbers//2+1


i=1:


