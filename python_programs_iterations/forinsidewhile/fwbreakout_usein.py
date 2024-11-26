i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
    i=i+1
#PROCESS
1.initilize i=1 for outerloop while range 1,2,3,4,5 if it is 6 then come out from outer loop or if condition satisfies then terminate
i=1 1<6 True
i=1,j=1 print(i,j)i.e o/p: 1 1 checks j==5 i.e 1==5 False
i=1,j=2 print(i,j)i.e o/p: 1 2 checks j==5 i.e 2==5 False
i=1,j=3 print(i,j)i.e o/p: 1 3 checks j==5 i.e 3==5 False
i=1,j=4 print(i,j)i.e o/p: 1 4 checks j==5 i.e 4==5 False
i=1,j=5 print(i,j)i.e o/p: 1 5 checks j==5 i.e 5==5 True outer loop has terminated

