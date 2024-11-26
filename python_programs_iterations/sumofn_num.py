#write a program to find sum of first n numbers
n=int(input("enter number"))
summ=0
for i in range(1,n+1):
    summ+=i
print(summ)
#process
"""
range starting value ll=1
range ending value ul=n+1 i.e n is 4 so n+1=5
1.Taking input from user for starting value i.e l because summ of 0 is 0 so for not wasting iteration we are taking starting range is 1
2.Taking input from user for ending value i.e 5 n+1 because input mentioned as n numers to get n numbers end range will be +1 i.e n+1
3.Assuming summ is 0 by thinking there is 0 sum with in the given range
3. fetch each and every value with in the range and add it to the summ

i=1: fetching as i=1 summ+=i so summ=0+1 summ=1
i=2: fetching as i=2 summ+=i so summ=1+2 summ=3
i=3: fetching as i=3 summ+=i so summ=3+3 summ=6
i=4: fetching as i=4 summ+=i so summ=6+4 summ=10
i=5: fetching as i=5 summ+=i so summ=10+5 summ=15

5.print the summ as 15 i.e summ=15
"""



