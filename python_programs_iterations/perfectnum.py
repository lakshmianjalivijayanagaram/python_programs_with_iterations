#write a program to find given number is perfect number or not
#perfect number : IF the number is eual to sum of its divisors then wecall it as  perfect number
num=int(input())
div_sum=0
for i in range(1,(num//2)+1):
    if num%i==0:
        div_sum+=i
if num==div_sum:
    print("pefect num")
else:
    print("not perfect")

#Process

"""
ex: num=6

1.taking input num from user i.e num ex num=6
2.Assuming that there no divisors for given num i.e div_sum=0
3. taking range for starting value is 1
end value is (num//2)+1 why because we exactly know that upto half of its value of num only have divisors for num for any number.
why num//2 is if we use "/" then we get float value range must be into so num//2 and 1 means we want num//2. if we give (num//2)+1 then we get upto (num//2)
so range(1,4) 6//2=3+1 i.e 4

i=1:  fetch i=1 checks num i.e 6%1==0 True so div_sum is incremented from 0 to 1.
i=2:  fetch i=2 checks num i.e 6%2==0 True so div_sum is incremented from 1 to 3.
i=3:  fetch i=3 checks num i.e 6%3==0 True so div_sum is incremented from 3 to 6.
range is upto 4 so 3 iteration from 1 to 4

4.checking num==6 and div_sum==6 i.e num==sum 6==6 True
5.print the output as "perfect number"

"""



