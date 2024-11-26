#w.r.t print given number disarim or not
#DIsarium number: when sum of its digits power of their respective positions equal to the number itself
#ex:135  135==1**1+3**2+5**3 True  ,89,518 are disarium numbers
n=int(input("enter the number "))
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ=summ+rem**l
    l=l-1
if(summ==n):
    print("****DISARIUM NUMBER****")
else:
    print("***NOT A DISARIUM NUMBER***")

#PROCESS
ex:   dummy=135
1.taking number input # for checking in future we need this so we are not changing
2.storing n in a dummy value for using further purpose
3.taking l as a variable to store the length of the input for num we cannot use len so num is coverted into str i.e len(str(n))
    why this because to use in power of individual element so
4.loop will run until dummy>0 

i=1: dummy=135 135>0 True
    rem=dummy%10 i.e rem=135%10 is o/p:5 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=135//10 i.e dummy=13 now dummy became reinitilized with the value
    summ=summ+rem**l i.e summ=0+5**3  sum=15 now we get sum for last digit with its respective index position
    NOW we are decrementing l for next value from last to get its index position
    i.e next value is 3 its index position is 2 l value is 3 now decremented to get 2 i.e l=2
    
i=2:dummy=13 13>0 True
     rem=13%10 i.e rem=3 based on this we will get individual digits of input
     dummy=13//10 dummy=1 dummy became reinitilized with the value
    summ=125+3**2 summ=134
    NOW we are decrementing l for next value from last to get its index position l=2-1 i.e l=1
    
i=3:dummy=1 1>0 True
    rem=1%10 i.e rem=1 based on this we will get individual digits of input
     dummy=1//10 dummy=0 dummy became reinitilized with the value
     summ=134+1**1 summ=135
     l=l-1 i.e 1-1=0
     
i=4: dummy=0 0>0 False
now come out from the loop
Now summ=135
checkhing if(135==135): True
o/p *****DISARIUM NUMBER*****
   
