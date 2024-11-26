#for is inside while
#complete exeution
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    i+=1
#PROCESS
1.outer loop while initialized with i=1 its range is 1,2,3,4,5 if it is 6 then will come out
i=1 i<6 i.e 1<6 enter into inner loop
i=1,j=1 print(i,j) o/p: 1 1
i=1,j=2 print(i,j) o/p: 1 2
i=1,j=3 print(i,j) o/p: 1 3
i=1,j=4 print(i,j) o/p: 1 4
i=1,j=5 print(i,j) o/p: 1 5 inner loop range done
outer loop j is incremented from 1 to 2


i=2 i<6 i.e 2<6 enter into inner loop
i=2,j=1 print(i,j) o/p: 2 1
i=2,j=2 print(i,j) o/p: 2 2
i=2,j=3 print(i,j) o/p: 2 3
i=2,j=4 print(i,j) o/p: 2 4
i=2,j=5 print(i,j) o/p: 2 5 inner loop range done
outer loop j is incremented from 2 to 3

i=3 i<6 i.e 3<6 enter into inner loop
i=3,j=1 print(i,j) o/p: 3 1
i=3,j=2 print(i,j) o/p: 3 2
i=3,j=3 print(i,j) o/p: 3 3
i=3,j=4 print(i,j) o/p: 3 4
i=3,j=5 print(i,j) o/p: 3 5 inner loop range done
outer loop j is incremented from 3 to 4

i=4 i<6 i.e 4<6 enter into inner loop
i=4,j=1 print(i,j) o/p: 4 1
i=4,j=2 print(i,j) o/p: 4 2
i=4,j=3 print(i,j) o/p: 4 3
i=4,j=4 print(i,j) o/p: 4 4
i=4,j=5 print(i,j) o/p: 4 5 inner loop range done
outer loop j is incremented from 4 to 5

i=5 i<6 i.e 5<6 enter into inner loop
i=5,j=1 print(i,j) o/p: 5 1
i=5,j=2 print(i,j) o/p: 5 2
i=5,j=3 print(i,j) o/p: 5 3
i=5,j=4 print(i,j) o/p: 5 4
i=5,j=5 print(i,j) o/p: 5 5 inner loop range done
outer loop j is incremented from 5 to 6

i=6 6>6 false come out from outer loop means outerloop range has done 






