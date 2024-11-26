#print given number is prime or not
#16-07-2024
n=int(input())
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print("n is not prime")
            break
    else:
        print("n is prime")
else:
    print("n is not a prime")

#using while
n=int(input())
if n>1:
    i=2
    while i<n//2+1:
        if n%i==0:
            print("n is not prime")
            break
        i+=1
    else:
        print("n is prime")
else:
    print("not a prime")

#Process
1.taking number as input to check prime or not
2.if input number is greater than 1 then only only we have to check the num is prime or not
    why because prime numbers starts from 2 onwards
3.if input num is not greater means less than or equal to 1 then it will directly goes to else block and prints output as "N NOT A PRIME"

#EX WHICH SATISFIES OUTER ELSE CONDITION
taking ex: num=1
    if n>1: false
SO go to else block and print output as "N IS NOT A PRIME"

#EXAMPLE WHICH SATISFIES AS A PRIME checking
TAKING EX: num=10
if n>1 True
so get into prime condition checking
range(2,6)  10//2+1 i.e 5+1=6
we have to check for i=2,3,4,5

i=1: fetch i=2  checks num%i==0 i.e 10%2==0 True so print as "NOT A PRIME" and then terminated
    which means if a number divisble by any number except 1,itself means not a prime
    if it is divisible by atleast no need to check with other number we can declare as" it is not a prime"
"10 IS NOT A PRIME"

#EXAMPLE WHICH SATISFIES AS A PRIME

TAKING EX: NUM=11
if n>1: true
now get into the loop and checks for whether it is prime or not
range(2,6) i.e n//2+1  11//2+1 ==5+1 i.e 6
we have to check for i=2,3,4,5

i=1: fetch i=2 checks 2<6 True checks num%i==0 11%2==0 False
i=2: fetch i=3 checks 3<6 True checks num%i==0 11%3==0 False
i=3: fetch i=4 checks 4<6 True checks num%i==0 11%4==0 False
i=4: fetch i=5 checks 5<6 True checks num%i==0 11%5==0 False
i=5: fetch i=6 #wont get because range is from (2,6)
**the loop is not terminated than goes to else lock and print output as "IT IS PRIME"

WE HAVE TO CHECK  ALL THE ITERATIONS FOR IT IS DIVISIBLE BY some number or not to check because than only we will get the number is  not divisible any one
so than only it will be declared as "IT IS PRIME"
i.e 11 is PRIME

#EX:2
if n>1: True
range is(2,2)
if lower and upper limits are same than wont enter into for loop goes to else directly prints as prime










