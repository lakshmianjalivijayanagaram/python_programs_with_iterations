#for is inside while 
#break inner loop use inner value
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
    i=i+1
#PROCESS
1.initilize i=1 for outerloop while range 1,2,3,4,5 if it is 6 then come out from uter loop
i=1 1<6 True  j in range 1,2,3,4,5 if it is 5 then come out from inner loop or condition satisfies then terminate
i=1,j=1 print(i,j) o/p:1 1  checks i==3 i.e 1==3 False
i=1,j=2 print(i,j) o/p:1 2  checks i==3 i.e 1==3 False
i=1,j=3 print(i,j) o/p:1 3  checks i==3 i.e 1==3 False
i=1,j=4 print(i,j) o/p:1 4  checks i==3 i.e 1==3 False
i=1,j=5 print(i,j) o/p:1 5  checks i==3 i.e 1==3 False inner loop range has done
outer loop j is incremented from 1 to 2

i=2 2<6 True
i=2,j=1 print(i,j) o/p:2 1  checks i==3 i.e 2==3 False
i=2,j=2 print(i,j) o/p:2 2  checks i==3 i.e 2==3 False
i=2,j=3 print(i,j) o/p:2 3  checks i==3 i.e 2==3 False
i=2,j=4 print(i,j) o/p:2 4  checks i==3 i.e 2==3 False
i=2,j=5 print(i,j) o/p:2 5  checks i==3 i.e 2==3 False inner loop range has done
outer loop j is incremented from 2 to 3

i=3 3<6 True
i=3,j=1 print(i,j) o/p:3 1  checks i==3 i.e 3==3 True so inner loop has terminated.nothing has done for outer loop
outer loop j is incremented from 3 to 4

i=4 4<6 True
i=4,j=1 print(i,j) o/p:4 1  checks i==3 i.e 4==3 False
i=4,j=2 print(i,j) o/p:4 2  checks i==3 i.e 4==3 False
i=4,j=3 print(i,j) o/p:4 3  checks i==3 i.e 4==3 False
i=4,j=4 print(i,j) o/p:4 4  checks i==3 i.e 4==3 False
i=4,j=5 print(i,j) o/p:4 5  checks i==3 i.e 4==3 False inner loop range has done
outer loop j is incremented from 4 to 5

i=5 5<6 True
i=5,j=1 print(i,j) o/p:5 1  checks i==3 i.e 5==3 False
i=5,j=2 print(i,j) o/p:5 2  checks i==3 i.e 5==3 False
i=5,j=3 print(i,j) o/p:5 3  checks i==3 i.e 5==3 False
i=5,j=4 print(i,j) o/p:5 4  checks i==3 i.e 5==3 False
i=5,j=5 print(i,j) o/p:5 5  checks i==3 i.e 5==3 False inner loop range has done
outer loop j is incremented from 5 to 6

i=6 6<6 False outer loop come out

