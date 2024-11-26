#print 10th niven/harshadnumbers
count=int(input())
n=1
hc=0
while True:
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ=summ+rem
    if(n%summ==0):
        hc+=1
        if hc==count:
            print(n)
            break
    n=n+1
#PROCESS
'''
1.taking count as input to give upto how many HARSHAD numbers you want
2.checking from number 1 so taking n=1
3.taking initially harshadnumber count as 0 i.e hc=0
3.taking infinite loop because we dont know upto which number  'n' harshadnumbers  we get.
4.we have number n input # for checking in future we need this so we are not changing
5.storing n in a dummy value for using further purpose
6.loop will run until dummy>0
count=5
i=1:n=1
    dummy=1
    summ=0
    while 1>0:
        rem=1%10 i.e 1
        dummy=1//10 i.e 0
        summ=0+1**1 i.e summ=1
    checks 1%1==0 True so
    hc is incremented from 0 to 1
    checks 1==5 false
    n is incremented from 1 to 2
i=2:n=2
    dummy=2
    summ=0
    while 2>0:
        rem=2%10 i.e 2
        dummy=2//10 i.e 0
        summ=0+2**1 i.e summ=2
    checks 2%2==0 True so
    hc is incremented from 1 to 2
    checks 2==5 false
    n is incremented from 2 to 3
i=3:n=3
    dummy=3
    summ=0
    while 3>0:
        rem=3%10 i.e 3
        dummy=3//10 i.e 0
        summ=0+3**1 i.e summ=3
    checks 3%3==0 True so print 3 and
    hc is incremented from 2 to 3
    checks 3==5 false
    n is incremented from 3 to 4
i=4:n=4
    dummy=4
    summ=0
    while 4>0:
        rem=4%10 i.e 4
        dummy=4//10 i.e 0
        summ=0+4**1 i.e summ=4
    checks 4%4==0 True so
    hc is incremented from 3 to 4
    checks 4==5 false
    n is incremented from 4 to 5
i=5:n=5
    dummy=5
    summ=0
    while 5>0:
        rem=5%10 i.e 5
        dummy=5//10 i.e 0
        summ=0+5**1 i.e summ=5
    checks 5%5==0 True so
    hc is incremented from 4 to 5
    checks 5==5 true
    print 5th number as 5
    loop has terminated
    
'''
