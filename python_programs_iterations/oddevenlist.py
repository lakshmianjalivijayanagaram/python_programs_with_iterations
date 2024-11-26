#10-07-2024
# i/p: l=[11,2,44,66,77]
# o/p: ['odd', 'even', 'even', 'even', 'odd']

l=[11,2,44,66,77]
for ip in range(len(l)):
    if l[ip]%2==0:
         l[ip]="even"
    else:
        l[ip]="odd"
print(l)

"""
l=[11,2,44,66,77]
l1=[]
for i in l:
    if i%2==0:
        l1.append("even")
    else:
        l1.append("odd")
print(l1)


l=[11,2,44,66,77]
l1=[]
for i in l:
    if i%2==0:
        l1+=["even"]
    else:
        l1+=["odd"]
print(l1)

"""        

#PROCESS:
"""
l=[11,2,44,66,77]

1.Given input is list
2.fetching each and every element and checking that element is even or odd

i=1: it will fetch ip=0 and l[ip]=11
checks l[ip]%2==0 i.e 11%2 False so replace l[0] with "odd" so l=["odd",2,44,66,77]

i=2: it will fetch ip=1 and l[ip]=22
checks l[ip]%2==0 i.e 22%2 True so replace l[0] with "even" so l=["odd","even",44,66,77]

i=3: it will fetch ip=3 and l[ip]=44
checks l[ip]%2==0 i.e 44%2 True so replace l[0] with "even" so l=["odd","even","even",66,77]

i=4: it will fetch ip=4 and l[ip]=66
checks l[ip]%2==0 i.e 66%2 True so replace l[0] with "even" so l=["odd","even","even","even",77]

i=5: it will fetch ip=5 and l[ip]=77
checks l[ip]%2==0 i.e 77%2 False so replace l[0] with "odd" so l=["odd","even","even","even","odd"]

3.After cmpletion of all the iteration print the output as
l=["odd","even","even","even","odd"]









