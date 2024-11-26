"""
#1.to print first 10 even numbers 
i=0
while i<20:
    print(i)
    i=i+2

#print even numbers in a given range
ll=int(input("enter ll val"))
ul=int(input("enter ul val"))
i=ll
while i<ul+1:
    if i%2==0:
        print(i)
    i+=1

#print to find sum of numbers within the range
ll=int(input())
ul=int(input())
i=ll
summ=0
while i<ul+1:
    summ+=i
    i=i+1
print(summ)

#to print sum of first n numbers
n=int(input())
i=1
summ=0
while i<n+1:
    summ+=i
    i=i+1
print(summ)

#print factorial of given number
num=int(input())
fact=1
i=1
while i<num+1:
    fact=fact*i
    i+=1
print(fact)


#program to find given number is perfect number or not
num=int(input())
sum_div=0
i=1
while i<(num//2)+1:
    if num%i==0:
        sum_div+=i
    i=i+1
if(num==sum_div):
    print("perfect")
else:
    print("not perfecet")


s="hello"
i=0
while i<len(s):
    print(s[i])
    i=i+1

#print the index positions where 'h' is present
s=input()
i=0
while i<len(s):
    if s[i]=="h":
        print(i)
    i=i+1


#print the elements present at even index positions
s=input()
i=0
while i<len(s):
        print(s[i])
        i=i+2


#write a program toprint the index psitions of vowel present in a string
s=input()
vowels="aeiouAEIOU"
i=0
while i<len(s):
        if s[i] in vowels:
                print(i)

        i=i+1


#write a program to replace all the vowels with their index positions
s=input()
vowels="aeiouAEIOU"
new=""
i=0
while i<len(s):
        if s[i] in vowels:
                new+=str(i)
        else:
                new+=s[i]
        i=i+1
print(new)


#program to print odd num present in odd index positions
s=input()
i=1
odd="13579"
while i<len(s):
        if s[i] in odd:
                print(s[i])
        i=i+2

s=input()
i=0
odd="13579"
while i<len(s):
        if s[i] in odd:
                print(s[i])
        i=i+2

s=input()
i=0
odd="02468"
while i<len(s):
        if s[i] in odd:
                print(s[i])
        i=i+2


s=input()
i=1
odd="02468"
while i<len(s):
        if s[i] in odd:
                print(s[i])
        i=i+2


#reverse a given string without using slicing
s=input()
i=0
rev=""
while i<len(s):
        rev=s[i]+rev
        i=i+1
print(rev)

#i/p: l=[11,2,44,66,77],o/p: ['odd', 'even', 'even', 'even', 'odd']

l=[11,2,44,66,77]
i=0
while i<len(l):
        if l[i]%2==0:
                l[i]="even"
        else:
                l[i]="odd"
        i=i+1
print(l)


l=[11,2,44,66,77]
i=0
li=[]
while i<len(l):
        if l[i]%2==0:
                li.append("even")
        else:
                li.append("odd")
        i=i+1
print(li)

#i/p: l=[11,22,33,44,55,66] o/p:l=[22,11,44,33,66,55]
l=[11,22,33,44,55,66]
i=0
while i<len(l):
        l[i],l[i+1]=l[i+1],l[i]
        i=i+2
print(l)

#impliment split method
s=input()
delimator=" "
dummy=""
l=[]
i=0
while i<len(s):
        if s[i]!=delimator:
                dummy=dummy+s[i]
        else:
                l.append(dummy)
                dummy=""
        i=i+1
l.append(dummy)
print(l)   

#reversing a string using while loop without using slicing
s=input()
rev=""
ip=-1
while ip>-(len(s)+1):
    rev+=s[ip]
    ip-=1
print(rev)

#impliment count method
s=input() 
sub=input()
c=0
ip=0
while ip<(len(s)-len(sub)+1):
    if s[ip:ip+len(sub)]==sub:
        c=c+1
    ip+=1
print(c)
"""























































