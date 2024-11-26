#for is inside while 
#break inner loop use inner value
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
    i=i+1
#PROCESS
1.initilize i=1 for outerloop while range 1,2,3,4,5 if it is 6 then come out from uter loop
i=1 1<6 True  j in range 1,2,3,4,5 if it is 5 then come out from inner loop or condition satisfies then terminate
i=1,j=1 print(i,j) i.e o/p: 1 1 checks j==3 i.e 1==3 false
i=1,j=2 print(i,j) i.e o/p: 1 2 checks j==3 i.e 2==3 false
i=1,j=3 print(i,j) i.e o/p: 1 3 checks j==3 i.e 3==3 True so innerloop terminates nothing will happen to outerloop
outer loop j is incremented from 1 to 2

i=2 2<6 True
i=2,j=1 print(i,j) i.e o/p: 2 1 checks j==3 i.e 1==3 false
i=2,j=2 print(i,j) i.e o/p: 2 2 checks j==3 i.e 2==3 false
i=2,j=3 print(i,j) i.e o/p: 2 3 checks j==3 i.e 3==3 True so innerloop terminates nothing will happen to outerloop
outer loop j is incremented from 2 to 3

i=2 3<6 True
i=3,j=1 print(i,j) i.e o/p: 3 1 checks j==3 i.e 1==3 false
i=3,j=2 print(i,j) i.e o/p: 3 2 checks j==3 i.e 2==3 false
i=3,j=3 print(i,j) i.e o/p: 3 3 checks j==3 i.e 3==3 True so innerloop terminates nothing will happen to outerloop
outer loop j is incremented from 3 to 4

i=2 4<6 True
i=4,j=1 print(i,j) i.e o/p: 4 1 checks j==3 i.e 1==3 false
i=4,j=2 print(i,j) i.e o/p: 4 2 checks j==3 i.e 2==3 false
i=4,j=3 print(i,j) i.e o/p: 4 3 checks j==3 i.e 3==3 True so innerloop terminates nothing will happen to outerloop
outer loop j is incremented from 4 to 5

i=2 5<6 True
i=5,j=1 print(i,j) i.e o/p: 5 1 checks j==3 i.e 1==3 false
i=5,j=2 print(i,j) i.e o/p: 5 2 checks j==3 i.e 2==3 false
i=5,j=3 print(i,j) i.e o/p: 5 3 checks j==3 i.e 3==3 True so innerloop terminates nothing will happen to outerloop
outer loop j is incremented from 5 to 6

i=6 6<6 False come out from the outer loop
