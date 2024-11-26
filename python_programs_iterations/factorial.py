#write a program to print factorial of given number
num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
#process

"""

n=4

range starting value ll=1
range ending value ul=n+1 i.e n is 4 so n+1=5


1.taking num value as input from user
2.we know that  factorial of 0 is 1 so assign fact=1
3Taking starting range as 1 why bacaue 0's factorial already taken 1 with fact and if taken here mutiply one with remaining get 0 also.
 Taking input from user for ending value i.e 4 n+1 because input mentioned as n numers to get n numbers end range will be +1 i.e n+1 i.e 5

3. fetch each and every value with in the range and multiply with fact to get factorial of given number

i=1: fetching as i=1 fact=fact*i i.e fact=1*1 so fact=1
i=2: fetching as i=2 fact=fact*2 i.e fact=1*2 so fact=2
i=3: fetching as i=3 fact=fact*3 i.e fact=2*3 so fact=6
i=4: fetching as i=4 fact=fact*4 i.e fact=6*4 so fact=24
"""
