"""n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**(len(str(n)))
if(summ==n):
    print("armstrong number")
else:
    print("not an armstrong number")
"""
n=int(input())
dummy=n
summ=0
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**(len(str(dummy))+1)
if(summ==n):
    print("disarium number")
else:
    print("not an disarium number")


