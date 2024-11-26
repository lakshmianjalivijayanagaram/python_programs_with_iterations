#Write a program to print the sum of indivual digits in a given number
n=int(input("enter the number"))
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ=summ+rem
print(summ)

#PROCESS:
"""
ex n:108
1.taking number input # for checking in future we need this so we are not changing
2.storing n in a dummy value for using further purpose
3.Assuming summ of the individual nums as 0
4.loop will run until dummy>0 

i=1: dummy=108 108>0 True
    rem=dummy%10 i.e rem=108%10 is o/p:8 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=108//10 i.e dummy=10 now dummy became reinitilized with the value
    summ=summ+rem i.e summ=0+8=8
i=2:dummy=10 10>0 True
    rem=dummy%10 i.e rem=1%10 is o/p:0 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=10//10 i.e dummy=1 now dummy became reinitilized with the value
    summ=summ+rem i.e summ=8+0=8
i=3:dummy=1 1>0 True
    rem=dummy%10 i.e rem=1%10 is o/p:1 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=1//10 i.e dummy=0 now dummy became reinitilized with the value
    summ=summ+rem i.e summ=8+1=9
i=4: dummy=0 0>0 false
come out fro the loop
print the output that is summ is 9
"""
