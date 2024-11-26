#write a program to print the perfect number within the given range
ll=int(input("enter a value"))
ul=int(input("enter a value"))
for num in range(ll,ul+1):
    summ=0
    for i in range(1,num//2+1):
        if num%i==0:
            summ+=i
    if summ==num:
        print(num)


#PROCESS
ll=4
ul=7
1.range is mentioned so taking ll and ul as 2 input
2.range is mentinoed we know how many times to executed that is within the range much times
3.Assuming summ as 0 that no number has divisors
4.taking inner for loop because we know the range means how many times to execute that is within the range much times i.e 1,num//2+1
num=4,i=1 checking range(1,3) i.e 4//2+1
now checking 4%1==0 True summ is incemented from 0 to 1
now checking 4%2==0 True summ is incremented from 1 to 3 range has done
checking that 3==4 False
outer range incremented from 4 to 5

num=5,i=1 checking range(1,3) i.e 4//2+1
now checking 5%1==0 True summ is incemented from 0 to 1
now checking 5%2==0 True summ is incremented from 1 to 3 range has done
checking that 3==5 False
outer range incremented from 5 to 6

num=6,i=1 checking range(1,4) i.e 6//2+1
now checking 6%1==0 True summ is incemented from 0 to 1
now checking 6%2==0 True summ is incremented from 1 to 3 
now checking 6%3==0 True summ is incremented from 3 to 6 range has done

checking that 6==6 True print 6 i.e o/p:6
outer range has done






