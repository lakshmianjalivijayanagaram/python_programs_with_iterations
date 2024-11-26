#for inside for
#break outer loop with outer loop value
#first checking next operation
for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
#PROCESS
1.for loop which is iterates for i=1,2,3,4,5
2.fetching outer for loop value then checks the condition if true terminates the entire loop
because the condition is for outer loop
now fetch i=1
i=1 checks if i==3 i.e 1==3 false so enter into inner for loop
    i=1, fetch j=1 print(i,j) i.e o/p:1 1
    i=1, fetch j=2 print(i,j) i.e o/p:1 2
    i=1, fetch j=3 print(i,j) i.e o/p:1 3
    i=1, fetch j=4 print(i,j) i.e o/p:1 4
    i=1, fetch j=5 print(i,j) i.e o/p:1 5

now fetch i=2
i=2 checks if i==3 i.e 2==3 false so enter into inner for loop
    i=2, fetch j=1 print(i,j) i.e o/p:2 1
    i=2, fetch j=2 print(i,j) i.e o/p:2 2
    i=2, fetch j=3 print(i,j) i.e o/p:2 3
    i=2, fetch j=4 print(i,j) i.e o/p:2 4
    i=2, fetch j=5 print(i,j) i.e o/p:2 5

now fetch i=3
i=3 checks if i==3 i.e 3==3 True

now the outer loop is terminated which means it is end no chance for further


#first peration next checking
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if i==3:
        break
#PROCESS
1.for loop which is iterates for i=1,2,3,4,5
fetch i=1
i=1,fetch j=1 print(i,j) i.e 1,1 
i=1,fetch j=2 print(i,j) i.e 1,2 
i=1,fetch j=3 print(i,j) i.e 1,3 
i=1,fetch j=4 print(i,j) i.e 1,4 
i=1,fetch j=5 print(i,j) i.e 1,5
Now checks i==3 i.e 1==3 False so continues iterations


fetch i=2
i=2,fetch j=1 print(i,j) i.e 2,1 
i=2,fetch j=2 print(i,j) i.e 2,2 
i=2,fetch j=3 print(i,j) i.e 2,3 
i=2,fetch j=4 print(i,j) i.e 2,4 
i=2,fetch j=5 print(i,j) i.e 2,5
Now checks i==3 i.e 2==3 False so continues iterations


fetch i=3
i=3,fetch j=1 print(i,j) i.e 3,1 
i=3,fetch j=2 print(i,j) i.e 3,2 
i=3,fetch j=3 print(i,j) i.e 3,3 
i=3,fetch j=4 print(i,j) i.e 3,4 
i=3,fetch j=5 print(i,j) i.e 3,5
Now checks i==3 i.e 3==3 True
now the outer loop is terminated so no chance for further iterations



























