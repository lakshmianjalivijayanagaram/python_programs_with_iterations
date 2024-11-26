#reverse a number
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    rev=rev*10+rem
print(rev)

#PROCESS
1.taking number input # for checking in future we need this so we are not changing
2.storing n in a dummy value for using further purpose
3.Assuming reverse of the number is 0
4.loop will run until dummy>0 

i=1: dummy=123 123>0 True
    rem=dummy%10 i.e rem=123%10 is o/p:3 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=123//10 i.e dummy=12 now dummy became reinitilized with the value
    rev=rev*10+rem i.e rev=0*10+3 i.e rev=3

i=2: dummy=12 12>0 True
    rem=dummy%10 i.e rem=12%10 is o/p:2 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=12//10 i.e dummy=1 now dummy became reinitilized with the value
    rev=rev*10+rem i.e rev=3*10+2 i.e rev=32

i=3: dummy=1 1>0 True
    rem=dummy%10 i.e rem=1%10 is o/p: based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=12//10 i.e dummy=0 now dummy became reinitilized with the value
    rev=rev*10+rem i.e rev=32*10+1 i.e rev=320+1 i.e rev=321
i=4: dummy=0 0>0 False
    come out from the loop
prints the rev value as 321


