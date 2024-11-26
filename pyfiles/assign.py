#10-07-2024


l=[11,22,33,44,-1,66,50]
l1=[]
for i in l:
    if i>0:
        if i%2==0:
            l1.append("even")
        else:
            l1.append("odd")
    else:
        l1.append(i)
print(l1)


#implement count method
s=input()
char=input()
count=0
for i in s:
    if i==char:
        count=count+1
print(count)


#implement split method

s=input()
deli=""
li=[]
s=""
for i in s:
    if i!=deli:
        s=s+i
        print(s)
    else:
        s.append(li)
        print(s)
print(s)
"""
