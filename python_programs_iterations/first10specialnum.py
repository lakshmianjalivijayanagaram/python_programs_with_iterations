#print first n special numbers
#special nummber 145==1!+4!+5!
count=int(input())
n=1
sc=0
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        summ=summ+fact
    if n==summ:
        print(n)
        sc+=1
        if sc==count:
            break

    n+=1
#PROCESS
'''1.taking count as input to give upto how many special numbers you want
2.checking from number 1 so taking n=1
3.taking special numbers count initially sc=0
4.taking infinite loop because we dont know upto which number  'n' armstrongnumbers  we get.
5.we have number n input # for checking in future we need this so we are not changing
6.storing n in a dummy value for using further purpose
7.taking l as a variable to store the length of the input for num we cannot use len so num is coverted into str i.e len(str(n))
   why this because to use in power of individual element when performing summ so
8.loop will run until dummy>0
i=1:n=1
    i=1:n=1
    dummy=1
    summ=0
    while 1>0:
        rem=1%10 i.e 1
        dummy=1//10 i.e 0
        fact=1
        fact in range(1,1) i.e(1,rem) range same so not enter into the loop
        directly summ=0+1 i.e summ=1
    checks 1==1:
        print 1
        sc incremented from 0 to 1
        1==5 false
        n is incremented from 1 to 2
i=2:n=2
    dummy=2
    summ=0
    while 2>0:
        rem=2%10 i.e 2
        dummy=2//10 i.e 0
        fact=1
        fact in range(1,2) i.e(1,rem) i.1 2!=2
        directly summ=0+2 i.e summ=2
    checks 2==2:
        print 2
        sc incremented from 1 to 2
        2==5 false
        n is incremented from 2 to 3
        and so on........................................................
        ............................................................
        ................................................................checked for other numbers those are not special numbers
n=145
dummy=145
summ=0
while 145>0:
    rem=145%10 i.e 5
    dummy=145//10 i.e 14
    fact=1
    for i in range(1,5+1) i.e (1,rem+1)
        fact=1*1=1
        fact=1*2=2
        fact=2*3=6
        fact=6*4=24
        fact=24*5=120 for range has done
    summ=0+120 i.e summ=120
while 14>0:
    rem=14%10 i.e 4
    dummy=14//10 i.e 1
    fact=1
    for i in range(1,4+1) i.e (1,rem+1)
        fact=1*1=1
        fact=1*2=2
        fact=2*3=6
        fact=6*4=24 for range has done
    summ=120+24 i.e summ=144

while 1>0:
    rem=1%10 i.e 1
    dummy=1//10 i.e 0
    fact=1
    for i in range(1,1+1) i.e (1,rem+1)
        fact=1*1=1 for range has done
    summ=144+1 i.e summ=145
checks 145==145:
        print 145
        sc incremented from 2 to 3
        3==5 false
        n is incremented from 145 to 146
    and so on....................................................
    ...............................................................
    ................................................

        like checking and gives upto first 10 values after getting 10 values terminates the loop
'''
