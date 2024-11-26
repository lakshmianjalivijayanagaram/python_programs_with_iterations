#write a program to print the prime number within the given range
ll=int(input("enter a value"))
ul=int(input("enter a value"))
for n in range(ll,ul+1):
    summ=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ+=rem**l
    if summ==n:
        print(n)
        
#PROCESS
ll=153
ul=155
1.range is mentioned so taking ll and ul as 2 input
2.range is mentinoed we know how many times to executed that is within the range that much times
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

checks summ==n i.e 153=153 True
    so print o/p:153

now outer loop value is incremented from 153 to 154
summ=0
dummy=n i.e dummy=154

i=1: dummy=154 154>0 True
    rem=dummy%10 i.e rem=154%10 is o/p:4 based on this we will get individual digits of input
    dummy=dummy//10 i.e dummy=154//10 i.e dummy=15 now dummy became reinitilized with the value
    summ=summ+rem**l i.e summ=0+4**3  sum=65 now we get sum for last digit by doing power of individual digit with its length of entire input
i=2:dummy=15 15>0 True
    rem=15%10 i.e rem=5 based on this we will get individual digits of input
    dummy=15//10 dummy=1 dummy became reinitilized with the value
    summ=64+5**3 summ=64+125 i.e summ=189
    
i=3:dummy=1 1>0 True
    rem=1%10 i.e rem=1 based on this we will get individual digits of input
    dummy=1//10 dummy=0 dummy became reinitilized with the value
    summ=189+1**1 summ=190
checks summ==n i.e 190=154 False
range has completed
    
    



