#for inside for
#break outer loop with inner loop value
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==3:
        break
#PROCESS
"""1.for loop which is iterates for i=1,2,3,4,5
fetch i=1
i=1, fetch j=1 print(i,j) o/p: 1,1
i=1, fetch j=2 print(i,j) o/p: 1,2
i=1, fetch j=3 print(i,j) o/p: 1,3
i=1, fetch j=4 print(i,j) o/p: 1,4
i=1, fetch j=5 print(i,j) o/p: 1,5
checks j==3 i.e 5==3 false so not terminated continue with next iterations

fetch i=2
i=2, fetch j=1 print(i,j) o/p: 2,1
i=2, fetch j=2 print(i,j) o/p: 2,2
i=2, fetch j=3 print(i,j) o/p: 2,3
i=2, fetch j=4 print(i,j) o/p: 2,4
i=2, fetch j=5 print(i,j) o/p: 2,5
checks j==3 i.e 5==3 false so not terminated continue with next iterations

fetch i=3
i=3, fetch j=1 print(i,j) o/p: 3,1
i=3, fetch j=2 print(i,j) o/p: 3,2
i=3, fetch j=3 print(i,j) o/p: 3,3
i=3, fetch j=4 print(i,j) o/p: 3,4
i=3, fetch j=5 print(i,j) o/p: 3,5
checks j==3 i.e 5==3 false so not terminated continue with next iterations

fetch i=4
i=4, fetch j=1 print(i,j) o/p: 4,1
i=4, fetch j=2 print(i,j) o/p: 4,2
i=4, fetch j=3 print(i,j) o/p: 4,3
i=4, fetch j=4 print(i,j) o/p: 4,4
i=4, fetch j=5 print(i,j) o/p: 4,5
checks j==3 i.e 5==3 false so not terminated continue with next iterations

fetch i=5
i=5, fetch j=1 print(i,j) o/p: 5,1
i=5, fetch j=2 print(i,j) o/p: 5,2
i=5, fetch j=3 print(i,j) o/p: 5,3
i=5, fetch j=4 print(i,j) o/p: 5,4
i=5, fetch j=5 print(i,j) o/p: 5,5
checks j==3 i.e 5==3 false so not terminated continue with next iterations

loop range has completed so no further iterations
 
"""
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
#PROCESS
1.for loop which is iterates for i=1,2,3,4,5
fetch i=1
i=1, fetch j=1 print(i,j) o/p: 1,1
i=1, fetch j=2 print(i,j) o/p: 1,2
i=1, fetch j=3 print(i,j) o/p: 1,3
i=1, fetch j=4 print(i,j) o/p: 1,4
i=1, fetch j=5 print(i,j) o/p: 1,5
checks j==5 i.e 5==5 True so terminated outer loop so no more further iterations





