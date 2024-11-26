#print first 10 perfect numbers 
#6,28,496
count=int(input())
n=1
pc=0
while True:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if summ==n:
        pc+=1
        if pc==count:
            print(n)
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
count=5
i=1:n=1
    i in range(1,1) i.e not enter into loop
    so summ=0
    checks 0==1 false
    n is incremented from 1 o 2
i=2:n=2
    i in range(1,2) 2%1==0 true
    so summ=1
    checks 2==1 false
    n is incremented from 2 o 3
    and so on........................still 6 we didnot get pefect val
i=6:n=6
    i in range(1,4)
    6%1==0 true summ=1
    6%2==0 true summ=1+2=3
    6%3==0 true summ=3+3 =6 for loop range has done
    checks 6==6 True so
    pc incremented from 0 to 1
    checks 1==5 false
    n value is incremented from 6 to 7
    and soo on .....................................
       it checks if pc==10 then print value then terminates the loop






    
'''

