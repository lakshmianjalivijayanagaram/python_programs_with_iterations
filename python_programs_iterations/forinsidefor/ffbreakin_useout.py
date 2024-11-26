#for inside for
#break inner loop with outer loop value

for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if i==3:
            break

#PROCESS
1.for loop which is iterates for i=1,2,3,4,5
2.fetching i=1 get inside the inner for loop print and checks the value for every iteration if the condition is satisfies
now fetch i=1
i=1:    i=1 fetch j=1 print(i,j) i.e o/p:1 1 checks i==3 i.e 1==3 False
        i=1 fetch j=2 print(i,j) i.e o/p:1 2 checks i==3 i.e 1==3 False
        i=1 fetch j=3 print(i,j) i.e o/p:1 3 checks i==3 i.e 1==3 False
        i=1 fetch j=4 print(i,j) i.e o/p:1 4 checks i==3 i.e 1==3 False
        i=1 fetch j=5 print(i,j) i.e o/p:1 5 checks i==3 i.e 1==3 False

fetch i=2
i=2:    i=2 fetch j=1 print(i,j) i.e o/p:2 1 checks i==3 i.e 2==3 False
        i=2 fetch j=2 print(i,j) i.e o/p:2 2 checks i==3 i.e 2==3 False
        i=2 fetch j=3 print(i,j) i.e o/p:2 3 checks i==3 i.e 2==3 False
        i=2 fetch j=4 print(i,j) i.e o/p:2 4 checks i==3 i.e 2==3 False
        i=2 fetch j=5 print(i,j) i.e o/p:2 5 checks i==3 i.e 2==3 False

fetch i=3
i=3:    i=3 fetch j=1 print(i,j) i.e o/p:3 1 checks i==3 i.e 3==3 True
        inner loop is terminated. it is inner loop termination so nothing will happens to outer loop so next iteration also be continued fo outer loop

fetch i=4
i=4:    i=4 fetch j=1 print(i,j) i.e o/p:3 1 checks i==3 i.e 4==3 False
        i=4 fetch j=2 print(i,j) i.e o/p:3 2 checks i==3 i.e 4==3 False
        i=4 fetch j=3 print(i,j) i.e o/p:3 3 checks i==3 i.e 4==3 False
        i=4 fetch j=4 print(i,j) i.e o/p:3 4 checks i==3 i.e 4==3 False
        i=4 fetch j=5 print(i,j) i.e o/p:3 5 checks i==3 i.e 4==3 False

fetch i=5
i=5:    i=5 fetch j=1 print(i,j) i.e o/p:5 1 checks i==3 i.e 5==3 False
        i=5 fetch j=2 print(i,j) i.e o/p:5 2 checks i==3 i.e 5==3 False
        i=5 fetch j=3 print(i,j) i.e o/p:5 3 checks i==3 i.e 5==3 False
        i=5 fetch j=4 print(i,j) i.e o/p:5 4 checks i==3 i.e 5==3 False
        i=5 fetch j=5 print(i,j) i.e o/p:5 5 checks i==3 i.e 5==3 False

4.Atlast both the outer loop and inner loop iterations has done
