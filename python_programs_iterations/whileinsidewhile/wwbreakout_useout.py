#while inside while
#brek outer loop with outer loop value
i=1
while i<6:
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        j=j+1
    i+=1
#PROCESS

1.initialize i=1 beause loop starts from 1 and for while loop user has to initialize value and iterations.
2.outer while loop has started with range 1,2,3,4,5,6 checks if i==3 conditions if true then terminates the entire outer loop
 now i=1
1<6 True checks i==3 i.e 1==3 false get into inside loop
j=1 1<6 print(i,j) i.e o/p: 1 1   j is increment from 1 to 2
j=2 2<6 print(i,j) i.e o/p: 1 2   j is increment from 2 to 3
j=3 3<6 print(i,j) i.e o/p: 1 3   j is increment from 3 to 4
j=4 4<6 print(i,j) i.e o/p: 1 4   j is increment from 4 to 5
j=5 5<6 print(i,j) i.e o/p: 1 5   j is increment from 5 to 6
j=6 6<6 false
i became incremented from 1 to 2

2<6 True checks i==3 i.e 2==3 false get into inner loop
j=1 1<6 print(i,j) i.e o/p: 2 1   j is increment from 1 to 2
j=2 2<6 print(i,j) i.e o/p: 2 2   j is increment from 2 to 3
j=3 3<6 print(i,j) i.e o/p: 2 3   j is increment from 3 to 4
j=4 4<6 print(i,j) i.e o/p: 2 4   j is increment from 4 to 5
j=5 5<6 print(i,j) i.e o/p: 2 5   j is increment from 5 to 6
j=6 6<6 false
i became incremented from 2 to 3

3<6 True checks i==3 i.e 3==3 True so entire outer loop became terminated. outer loop terminated means no more further iterations.  



