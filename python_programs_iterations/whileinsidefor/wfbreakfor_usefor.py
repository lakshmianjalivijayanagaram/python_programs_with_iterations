#while is inside for
#break inner loop using outer loop value
for i in range(1,6):
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        j=j+1
#PROCESS
1.for loop in range of 1,2,3,4,5 it the range is 5 then it will stop ot the condition is satisfies then it will stop
i=1 checks i==3 i.e 1==3 False
i=1, j=1  j<6 i.e 1<6 True print(i,j) i.e 1,1 j is incremented from 1 to 2
i=1, j=2  j<6 i.e 2<6 True print(i,j) i.e 1,2 j is incremented from 2 to 3
i=1, j=3  j<6 i.e 3<6 True print(i,j) i.e 1,3 j is incremented from 3 to 4
i=1, j=4  j<6 i.e 4<6 True print(i,j) i.e 1,4 j is incremented from 4 to 5
i=1, j=5  j<6 i.e 5<6 True print(i,j) i.e 1,5 j is incremented from 5 to 6
i=1, j=6  j<6 i.e 6<6 false come out from inner loop

i=2 checks i==3 i.e 2==3 False
i=2, j=1  j<6 i.e 1<6 True print(i,j) i.e 2,1 j is incremented from 1 to 2
i=2, j=2  j<6 i.e 2<6 True print(i,j) i.e 2,2 j is incremented from 2 to 3
i=2, j=3  j<6 i.e 3<6 True print(i,j) i.e 2,3 j is incremented from 3 to 4
i=2, j=4  j<6 i.e 4<6 True print(i,j) i.e 2,4 j is incremented from 4 to 5
i=2, j=5  j<6 i.e 5<6 True print(i,j) i.e 2,5 j is incremented from 5 to 6
i=2, j=6  j<6 i.e 6<6 false come out from inner loop

i=3 checks i==3 i.e 3==3 True so outer loop has terminated         
