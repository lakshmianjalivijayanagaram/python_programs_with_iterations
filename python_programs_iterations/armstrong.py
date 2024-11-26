#w.r.t print given number is armstrong number or not
#armstrong number is 153=1**3+5**3+3**3
n=int(input("enter a number "))
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**l
if n==summ:
    print("********armstrong number*****")
else:
    print("****not an armstrong number******")

#PROCESS:

ex: dummy=153
1.taking number input # for checking in future we need this so we are not changing
2.storing n in a dummy value for using further purpose
3.taking l as a variable to store the length of the input for num we cannot use len so num is coverted into str i.e len(str(n))
    why this because to use in power of individual element when performing summ so
4.loop will run until dummy>0 

i=1: dummy=153 153>0 True
    rem=dummy%10 i.e rem=153%10 is o/p:3 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=153//10 i.e dummy=15 now dummy became reinitilized with the value
    summ=summ+rem**l i.e summ=0+3**3  sum=27 now we get sum for last digit by doing power of individual digit with its length of entire input
       
i=2:dummy=15 15>0 True
     rem=15%10 i.e rem=5 based on this we will get individual digits of input
     dummy=15//10 dummy=1 dummy became reinitilized with the value
    summ=27+5**3 summ=152
    
i=3:dummy=1 1>0 True
    rem=1%10 i.e rem=1 based on this we will get individual digits of input
     dummy=1//10 dummy=0 dummy became reinitilized with the value
     summ=152+1**1 summ=153

i=4: dummy=0 0>0 False
now come out from the loop
Now summ=153
checkhing if(153==153): True
o/p *****armstrong NUMBER*****

     

