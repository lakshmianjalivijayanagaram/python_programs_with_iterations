#write a program to print the prime number within the given range
ll=int(input("enter a value"))
ul=int(input("enter a value"))
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
    
#PROCESS
ll=2
ul=7
1.range is mentioned so taking ll and ul as 2 input
2.range is mentinoed we know how many times to executed that is within the range that much times
3.we know that one condition is the prime is start from 2 only so we are giving a ondition that it would be greater than 1
4.taking inner for loop because we know the range means how many times to execute that is within the range much times i.e 1,n//2+1
now n=2 range to check is(2,2)
range is same so it wont enter into the directly print as o/p:2
outer loop incremented from 2 to 3

now n=3 range to check is(2,2)
range is same so it wont enter into the directly print as o/p:3
outer loop incremented from 3 to 4

now n=4 range to check is(2,3) i=2
checks 4%2==0 True innerloop terminates nothing will happen to outerloop
outer loop incremented from 4 to 5

now n=5 range to check is(2,3) i=2
checks 5%2==0 False range has completed condition not true come out from innerloop
print output as o/p:5 
outer loop incremented from 5 to 6

now n=6 range to check is(2,4) i=2
checks 6%2==0 True innerloop terminates nothing will happen to outerloop
outer loop incremented from 6 to 7

outer loop range has completed








