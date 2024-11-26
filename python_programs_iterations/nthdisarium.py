#print 10th disariumnumbers
#special nummber 145==1!+4!+5!

count=int(input())
n=1
dc=0
while True:
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
        l-=1
    if summ==n:
        dc+=1
    if dc==count:
        print(n)
        break
    n+=1

#process
'''1.taking count as input to give upto how many armstrong numbers you want
2.checking from number 1 so taking n=1
3.4.taking infinite loop because we dont know upto which number  'n' armstrongnumbers  we get.
4.we have number n input # for checking in future we need this so we are not changing
5.storing n in a dummy value for using further purpose
6.taking l as a variable to store the length of the input for num we cannot use len so num is coverted into str i.e len(str(n))
   why this because to use in power of individual element when performing summ so
7.loop will run until dummy>0
count=5

i=1:n=1
    dummy=1
    summ=0
    while 1>0:
        rem=1%10 i.e 1
        dummy=1//10 i.e 0
        summ=0+1**1 i.e summ=1
        l-=1 i.e 1-1=0
    checks 1==1: True
    so dc is incremented 0 to 1
    checks 1==5 false
    so n is incremented from 1 to 2

i=2:n=2
    dummy=2
    summ=0
    while 2>0:
        rem=2%10 i.e 2
        dummy=2//10 i.e 0
        summ=0+2**1 i.e summ=2
        l-=1 i.e 1-1=0
    checks 2==2: True
    so dc is incremented 1 to 2
    checks 2==5 false
    so n is incremented from 2 to 3
i=3:n=3
    dummy=3
    summ=0
    while 3>0:
        rem=3%10 i.e 3
        dummy=3//10 i.e 0
        summ=0+3**1 i.e summ=3
        l-=1 i.e 1-1=0
    checks3==3: True
    so dc is incremented 2 to 3
    checks 3==5 false
    so n is incremented from 3 to 4
i=4:n=4
    dummy=4
    summ=0
    while 4>0:
        rem=4%10 i.e 4
        dummy=4//10 i.e 0
        summ=0+4**1 i.e summ=4
        l-=1 i.e 1-1=0
    checks 4==4: True
    so is incremented 3 to 4
    checks 4==5 false
    so n is incremented from 4 to 5

i=5:n=5
    dummy=5
    summ=0
    while 5>0:
        rem=5%10 i.e 5
        dummy=5//10 i.e 0
        summ=0+5**1 i.e summ=5
        l-=1 i.e 1-1=0
    checks 5==5: True
    so dc is incremented 4 to 5
    checks 5==5 True
    so print 5th value as 5
    and terminates the loop

'''
