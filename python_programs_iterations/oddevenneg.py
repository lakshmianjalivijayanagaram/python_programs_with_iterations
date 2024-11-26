#10-07-2024
# i/p: l=[11,22,33,44,-1,66,50]
# o/p: ['odd', 'even',"odd",'even',-1, 'even', 'even']

l=[11,22,33,44,-1,66,50]
for ip in range(len(l)):
    if l[ip]>0:
        if l[ip]%2==0:
             l[ip]="even"
        else:
            l[ip]="odd"
print(l)


#PROCESS:
"""
i/p: l=[11,22,33,44,-1,66,50]

1.Given input is list
2.fetching each and every element and checking that element is even or odd

i=1: it will fetch ip=0 and l[ip]=11 
checks l[ip]>0 true so checks l[ip]%2==0 i.e 11%2 False so replace l[0] with "odd" so l=["odd",22,33,44,-1,66,50]

i=2: it will fetch ip=1 and l[ip]=22 
checks l[ip]>0 true so checks l[ip]%2==0 i.e 22%2 True so replace l[1] with "even" so l=["odd","even",33,44,-1,66,50]

i=3: it will fetch ip=2 and l[ip]=33
checks l[ip]>0 true so checks l[ip]%2==0 i.e 33%2 False so replace l[2] with "odd" so l=["odd","even","odd",44,-1,66,50]

i=4: it will fetch ip=3 and l[ip]=44
checks l[ip]>0 true so checks l[ip]%2==0 i.e 44%2 True so replace l[3] with "even" so l=["odd","even","odd","even",-1,66,50]

i=5: it will fetch ip=4 and l[ip]=-1
checks l[ip]>0 False

i=6: it will fetch ip=5 and l[ip]=66
checks l[ip]>0 true so checks l[ip]%2==0 i.e 66%2 True so replace l[5] with "even" so l=["odd","even","odd","even",-1,"even",50]

i=7: it will fetch ip=6 and l[ip]=50
checks l[ip]>0 true so checks l[ip]%2==0 i.e 50%2 True so replace l[6] with "even" so l=["odd","even","odd","even",-1,"even","even"]



3.After cmpletion of all the iteration print the output as
i.e l=["odd","even","odd","even",-1,"even","even"]
"""
