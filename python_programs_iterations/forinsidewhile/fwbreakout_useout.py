#for is inside while 
#break inner loop use inner value
i=1
while i<6:
    if i==3:
        break
    for j in range(1,6):
        print(i,j)

    i=i+1
    
#PROCESS
1.initilize i=1 for outerloop while range 1,2,3,4,5 if it is 6 then come out from outer loop or if condition satisfies then terminate
i=1 i<6 i.e 1<6 True
i=1 checks i==3 i.e 1==3 False
i=1,j=1 print(i,j) o/p:1 1
i=1,j=2 print(i,j) o/p:1 2
i=1,j=3 print(i,j) o/p:1 3
i=1,j=4 print(i,j) o/p:1 4
i=1,j=5 print(i,j) o/p:1 5 inner loop range has done
i is incremented from 1 to 2

i=2 i<6 i.e 2<6 True
i=2 checks i==3 i.e 2==3 False
i=2,j=1 print(i,j) o/p:2 1
i=2,j=2 print(i,j) o/p:2 2
i=2,j=3 print(i,j) o/p:2 3
i=2,j=4 print(i,j) o/p:2 4
i=2,j=5 print(i,j) o/p:2 5 inner loop range has done
i is incremented from 2 to 3

i=3 i<6 i.e 3<6 True
i=3 checks i==3 i.e 3==3 True outer loop is terminated


