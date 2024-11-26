#18-07-2024
#while inside while
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    i+=1
#PROCESS
1.initialize i=1 beause loop starts from 1 and for while loop user has to initialize value and iterations.
2.outer while loop has started with range 1,2,3,4,5,6 if it is 6 it will come out
3.iitialize inner while loop j=1  and for while loop user has to initialize value and iterations.
4.inner while loop has started with range 1,2,3,4,5,6 if it is 6 it will come out
now i=1,j=1 checks 1<6 False print(i,j) i.e 1 1 j increment from 1 to 2 j=2
checks 2>6 False    i=1,j=2 print(i,j) i.e 1 2 j increment from 2 to 3 j=3
checks 3>6 False    i=1,j=3 print(i,j) i.e 1 3 j increment from 3 to 4 j=4
checks 4>6 False    i=1,j=4 print(i,j) i.e 1 4 j increment from 4 to 5 j=5
checks 4>6 False    i=1,j=5 print(i,j) i.e 1 5 j increment from 5 to 6 j=6
checks 6>6 True come out from inner loop
outer loop variable i.e i became incremented from 1 to 2

Now i=2
checks 2<6 False get inside inner loop
i=2,j=1 checks 1<6 False print(i,j) i.e 2 1 j increment from 1 to 2 j=2
checks 2>6 False    i=2,j=2 print(i,j) i.e 2 2 j increment from 2 to 3 j=3
checks 3>6 False    i=2,j=3 print(i,j) i.e 2 3 j increment from 3 to 4 j=4
checks 4>6 False    i=2,j=4 print(i,j) i.e 2 4 j increment from 4 to 5 j=5
checks 4>6 False    i=2,j=5 print(i,j) i.e 2 5 j increment from 5 to 6 j=6
checks 6>6 True come out from inner loop
outer loop variable i.e i became incremented from 2 to 3

Now i=3
checks 3<6 False get inside inner loop
i=3,j=1 checks 1<6 False print(i,j) i.e 3 1 j increment from 1 to 2 j=2
checks 2>6 False    i=3,j=2 print(i,j) i.e 3 2 j increment from 2 to 3 j=3
checks 3>6 False    i=3,j=3 print(i,j) i.e 3 3 j increment from 3 to 4 j=4
checks 4>6 False    i=3,j=4 print(i,j) i.e 3 4 j increment from 4 to 5 j=5
checks 4>6 False    i=3,j=5 print(i,j) i.e 3 5 j increment from 5 to 6 j=6
checks 6>6 True come out from inner loop
outer loop variable i.e i became incremented from 3 to 4

Now i=4
checks 4<6 False get inside inner loop
i=4,j=1 checks 1<6 False print(i,j) i.e 4 1 j increment from 1 to 2 j=2
checks 2>6 False    i=4,j=2 print(i,j) i.e 4 2 j increment from 2 to 3 j=3
checks 3>6 False    i=4,j=3 print(i,j) i.e 4 3 j increment from 3 to 4 j=4
checks 4>6 False    i=4,j=4 print(i,j) i.e 4 4 j increment from 4 to 5 j=5
checks 4>6 False    i=4,j=5 print(i,j) i.e 4 5 j increment from 5 to 6 j=6
checks 6>6 True come out from inner loop
outer loop variable i.e i became incremented from 4 to 5

Now i=5
checks 5<6 False get inside inner loop
i=5,j=1 checks 1<6 False print(i,j) i.e 5 1 j increment from 1 to 2 j=2
checks 2>6 False    i=5,j=2 print(i,j) i.e 5 2 j increment from 2 to 3 j=3
checks 3>6 False    i=5,j=3 print(i,j) i.e 5 3 j increment from 3 to 4 j=4
checks 4>6 False    i=5,j=4 print(i,j) i.e 5 4 j increment from 4 to 5 j=5
checks 4>6 False    i=5,j=5 print(i,j) i.e 5 5 j increment from 5 to 6 j=6
checks 6>6 True come out from inner loop
outer loop variable i.e i became incremented from 5 to 6

now i=6
checks 6>6 False
come out from outer loop no more further itertions 

 
