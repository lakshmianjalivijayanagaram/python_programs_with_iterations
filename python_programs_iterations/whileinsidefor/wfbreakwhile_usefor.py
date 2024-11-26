#while is inside for
#break inner loop using outer loop value
for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j=j+1

#PROCESS

1.for loop in range of 1,2,3,4,5 it the range is 5 then it will stop
2.initialize j=1 for inner while loop
3.inner while in range 1,2,3,4,5 if the condition satisfies it will end innerloop or if it is 6 then it will come out from innerloop
i=1,j=1 j<6 i.e 1<6 True print(i,j) i.e o/p: 1 1 checks i==3 i.e 1==3 false j is incremented from 1 to 2
i=1,j=2 j<6 i.e 2<6 True print(i,j) i.e o/p: 1 2 checks i==3 i.e 1==3 false j is incremented from 2 to 3
i=1,j=3 j<6 i.e 3<6 True print(i,j) i.e o/p: 1 3 checks i==3 i.e 1==3 false j is incremented from 3 to 4
i=1,j=4 j<6 i.e 4<6 True print(i,j) i.e o/p: 1 4 checks i==3 i.e 1==3 false j is incremented from 4 to 5
i=1,j=5 j<6 i.e 5<6 True print(i,j) i.e o/p: 1 5 checks i==3 i.e 1==3 false j is incremented from 5 to 6
i=1,j=6 j<6 i.e 6<6 false come out from inner loop

i=2,j=1 j<6 i.e 1<6 True print(i,j) i.e o/p: 2 1 checks i==3 i.e 2==3 false j is incremented from 1 to 2
i=2,j=2 j<6 i.e 2<6 True print(i,j) i.e o/p: 2 2 checks i==3 i.e 2==3 false j is incremented from 2 to 3
i=2,j=3 j<6 i.e 3<6 True print(i,j) i.e o/p: 2 3 checks i==3 i.e 2==3 false j is incremented from 3 to 4
i=2,j=4 j<6 i.e 4<6 True print(i,j) i.e o/p: 2 4 checks i==3 i.e 2==3 false j is incremented from 4 to 5
i=2,j=5 j<6 i.e 5<6 True print(i,j) i.e o/p: 2 5 checks i==3 i.e 2==3 false j is incremented from 5 to 6
i=2,j=6 j<6 i.e 6<6 false come out from inner loop

i=3,j=1 j<6 i.e 1<6 True print(i,j) i.e o/p: 3 1 checks i==3 i.e 3==3 True inner loop is terminated but nothing will happen to outer loop

i=4,j=1 j<6 i.e 1<6 True print(i,j) i.e o/p: 4 1 checks i==3 i.e 4==3 false j is incremented from 1 to 2
i=4,j=2 j<6 i.e 2<6 True print(i,j) i.e o/p: 4 2 checks i==3 i.e 4==3 false j is incremented from 2 to 3
i=4,j=3 j<6 i.e 3<6 True print(i,j) i.e o/p: 4 3 checks i==3 i.e 4==3 false j is incremented from 3 to 4
i=4,j=4 j<6 i.e 4<6 True print(i,j) i.e o/p: 4 4 checks i==3 i.e 4==3 false j is incremented from 4 to 5
i=4,j=5 j<6 i.e 5<6 True print(i,j) i.e o/p: 4 5 checks i==3 i.e 4==3 false j is incremented from 5 to 6
i=4,j=6 j<6 i.e 6<6 false come out from inner loop

i=5,j=1 j<6 i.e 1<6 True print(i,j) i.e o/p: 5 1 checks i==3 i.e 5==3 false j is incremented from 1 to 2
i=5,j=2 j<6 i.e 2<6 True print(i,j) i.e o/p: 5 2 checks i==3 i.e 5==3 false j is incremented from 2 to 3
i=5,j=3 j<6 i.e 3<6 True print(i,j) i.e o/p: 5 3 checks i==3 i.e 5==3 false j is incremented from 3 to 4
i=5,j=4 j<6 i.e 4<6 True print(i,j) i.e o/p: 5 4 checks i==3 i.e 5==3 false j is incremented from 4 to 5
i=5,j=5 j<6 i.e 5<6 True print(i,j) i.e o/p: 5 5 checks i==3 i.e 5==3 false j is incremented from 5 to 6
i=5,j=6 j<6 i.e 6<6 false come out from inner loop
outer loop range has completed

