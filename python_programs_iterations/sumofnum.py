#write a program to print even numbers in given range
ll=int(input("enter number"))
ul=int(input("enter number"))
summ=0
for i in range(ll,ul+1):
    summ+=i
    print(summ)
#process
"""
ll=1
ul=6
1.Taking input from user for starting value i.e l because in the input range is not mentioned
2.Taking input from user for ending value i.e 6 because in the input range is not mentioned
3.Assuming summ is 0 by thinking there is 0 sum with in the given range
3. fetch each and every value with in the range and checks whether it is even or not

i=1: fetching as i=1 summ+=i so summ=0+1 summ=1
i=2: fetching as i=2 summ+=i so summ=1+2 summ=3
i=3: fetching as i=3 summ+=i so summ=3+3 summ=6
i=4: fetching as i=4 summ+=i so summ=6+4 summ=10
i=5: fetching as i=5 summ+=i so summ=10+5 summ=15

5.print the summ as 15 i.e summ=15
"""



