#special number
#if 145=5!+4!+1! special number
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    summ+=fact
if n==summ:
    print("special number")
else:
    print("not special number")
        
#PROCESS
1.taking initial value as 1
2.assuming special operators count as 0 i.e sc=0
3.taking infinity loop because we dont know how many times to iterate
4.enter into outer while
5.Assuming summ of individual digits factors as 0
6.storing n in dummy variable because we are changing
7.checking while dummy>0:

i=1:145>0:TRUE
    rem=145%10  i.e o/p:5
    dummy=145//10 i.e o/p:5
    #for finding factorial of indivial number so performing factorial operation
    fact=1
    #using for loop because we know factors range
        i in range(1,5+1):
            now i=1
            fact=1*i i.e fact=1*1 i.e fact=1
            i=2
            fact=1*i i.e fact=1*1 i.e fact=2
            i=3
            fact=1*i i.e fact=2*3 i.e fact=6
            i=4
            fact=1*i i.e fact=4*6 i.e fact=24
            i=5
            fact=1*i i.e fact=24*5 i.e fact=120
        for range has completed
        summ+=120 i.e summ=0+120 o/p:120
i=2:14>0:TRUE
    rem=14%10  i.e o/p:4
    dummy=14//10 i.e o/p:1
    #for finding factorial of indivial number so performing factorial operation
    fact=1
    #using for loop because we know factors range
        i in range(1,4+1):
            now i=1
            fact=1*i i.e fact=1*1 i.e fact=1
            i=2
            fact=1*i i.e fact=1*1 i.e fact=2
            i=3
            fact=1*i i.e fact=2*3 i.e fact=6
            i=4
            fact=1*i i.e fact=4*6 i.e fact=24
        for range has completed
        summ+=120 i.e summ=120+24 o/p:144
i=3:1>0:TRUE
    rem=1%10  i.e o/p:1
    dummy=1//10 i.e o/p:0
    #for finding factorial of indivial number so performing factorial operation
    fact=1
    #using for loop because we know factors range
        i in range(1,2):
            now i=1
            fact=1*i i.e fact=1*1 i.e fact=1
            
        for range has completed
        summ+=120 i.e summ=144+1 o/p:145
i=4 0>0 false
come out from the loop
checks summ==n i.e 145==145 true
prints as special number

        
