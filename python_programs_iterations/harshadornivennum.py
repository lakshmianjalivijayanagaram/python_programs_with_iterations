#write a program to print given number is niven/harshad number or not
#harshad number:it is a number which is divisible by sum of its individual digits
#ex: 12 i.e 1+2=3   12%3==0 true it is niven

n=int(input("enter the number"))
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ=summ+rem
if(n%summ==0):
    print("niven/harshad number")
else:
   print("not niven/harshad number")

#PROCESS:
ex n:12
1.taking number input # for checking in future we need this so we are not changing
2.storing n in a dummy value for using further purpose
3.Assuming SUMm of the individual nums as 0
4.loop will run until dummy>0 

i=1: dummy=12 12>0 True
    rem=dummy%10 i.e rem=12%10 is o/p:2 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=12//10 i.e dummy=1 now dummy became reinitilized with the value
    summ=summ+rem i.e summ=0+2=2
i=2:dummy=1 1>0 True
    rem=dummy%10 i.e rem=1%10 is o/p:1 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=1//10 i.e dummy=0 now dummy became reinitilized with the value
    summ=summ+rem i.e summ=2+1=3
i=3: dummy=0 0>0 false
come out from the loop
checks 12%==0 true
prints the output as "niven/harshad number"

    
