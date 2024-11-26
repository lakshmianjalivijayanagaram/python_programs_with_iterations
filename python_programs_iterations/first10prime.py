#print the first n prime numbers in a given range
count=int(input())
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
        if pc==count:
            break
    n=n+1
#process

"""
1.taking input count for upto how many count we need values
2.taking values from n=1 because from 1 onwards we are checking for primes
3.counting prime numbers so initially it is pc=0
4.taking infinite loop because we dont know upto which number first 'n' primes we get.
5.if the number is greater than 1 then only it is a prime so before checking for prime we are giving condition that is n>1
count=4
n=1:
i=1:checks n>1 false
directly increment n value beause it is not capable for checking also

i=2:now n=2:
checks n>1 true
range(2,2) no range go to else print 2 incremented pc count from 0 to 1
and checks my pc==count i.e 1==5 false so
increment n value from 2 to 3

i=3:now n=3
checks n>1 true
range(2,2) no range go to else print 3 incremented pc count from 1 to 2
and checks my pc==count i.e 2==5 false so
increment n value from 3 to 4

i=4:now n=4
checks n>1 true
range(2,3) checks 4%2==0 true so break inner loop now
increment n value from 4 to 5

i=5:now n=5
checks n>1 true
range(2,3) checks 5%2==0 false
come to forelse and print 5 count beacame incremented from 2 to 3
checks my pc==count i.e 3==5 false so
increment n value from 5 to 6

i=6:now n=6
checks n>1 true
range(2,4) checks 6%2==0 true so break inner loop now
increment n value from 6 to 7

i=7:now n=7
checks n>1 true
range(2,4) checks 7%2==0 false 7%3==0 false
come to forelse and print 7 count became incremented from 3 to 4
checks my pc==count i.e 4==4 true so break the entire loop





