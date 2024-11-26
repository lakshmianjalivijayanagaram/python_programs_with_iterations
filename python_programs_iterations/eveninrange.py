#write a program to print even numbers in given range
ll=int(input("enter number"))
ul=int(input("enter number"))
for i in range(ll,ul+1):
    if i%2==0:
print(i)
#process
"""
ll=1
ul=10
1.Taking input from user for starting value i.e l because in the input range is not mentioned
2.Taking input from user for ending value i.e l0 because in the input range is not mentioned
3. fetch each and every value with in the range and checks whether it is even or not

i=1: fetching as i=1 checks i i.e 1%2==0 False
i=2: fetching as i=2 checks i i.e 2%2==0 true so prints 2
i=3: fetching as i=3 checks i i.e 3%2==0 False
i=4: fetching as i=4 checks i i.e 4%2==0 true so prints 4
i=5: fetching as i=5 checks i i.e 5%2==0 False
i=6: fetching as i=6 checks i i.e 6%2==0 true so prints 6
i=7: fetching as i=7 checks i i.e 7%2==0 False
i=8: fetching as i=8 checks i i.e 8%2==0 true so prints 8
i=7: fetching as i=9 checks i i.e 9%2==0 False

o/p:2,4,6,8
"""



