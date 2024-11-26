#18-07-2024
#while inside while
#break inner loop using inner loop value
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j=j+1
    i=i+1

#PROCESS
1.initialize i=1 beause loop starts from 1 and for while loop user has to initialize value and iterations.
2.outer while loop has started with range 1,2,3,4,5,6 if it is 6 it will come out
3.iitialize inner while loop j=1  and for while loop user has to initialize value and iterations.
4.inner while loop has started with range 1,2,3,4,5,6 if it is 6 it will come out then perform operation if condition True than terminate inner loop
    otherwise continues
i=1 checks 1<6 True then enter into outer loop
i=1,j=1 checks 1<6 True so print(i,j) i.e 1 1 checks j==3  i.e 1==3 false j became incremented from 1 to 2 
i=1,j=2 checks 2<6 True so print(i,j) i.e 1 2 checks j==3  i.e 2==3 false j became incremented from 2 to 3
i=1,j=3 checks 3<6 True so print(i,j) i.e 1 3 checks j==3  i.e 3==3 True so terminated inner loop but nothing happens to outer loop.means outer loop became incremented
i is incremented from 1 to 2

i=2 checks 2<6 True then enter into outer loop
i=2,j=1 checks 1<6 True so print(i,j) i.e 2 1 checks j==3  i.e 1==3 false j became incremented from 1 to 2 
i=2,j=2 checks 2<6 True so print(i,j) i.e 2 2 checks j==3  i.e 2==3 false j became incremented from 2 to 3
i=2,j=3 checks 3<6 True so print(i,j) i.e 2 3 checks j==3  i.e 3==3 True so terminated inner loop but nothing happens to outer loop.means outer loop became incremented
i is incremented from 2 to 3

i=3 checks 3<6 True then enter into outer loop
i=3,j=1 checks 1<6 True so print(i,j) i.e 3 1 checks j==3  i.e 1==3 false j became incremented from 1 to 2 
i=3,j=2 checks 2<6 True so print(i,j) i.e 3 2 checks j==3  i.e 2==3 false j became incremented from 2 to 3
i=3,j=3 checks 3<6 True so print(i,j) i.e 3 3 checks j==3  i.e 3==3 True so terminated inner loop but nothing happens to outer loop.means outer loop became incremented
i is incremented from 3 to 4

i=4 checks 4<6 True then enter into outer loop
i=4,j=1 checks 1<6 True so print(i,j) i.e 4 1 checks j==3  i.e 1==3 false j became incremented from 1 to 2 
i=4,j=2 checks 2<6 True so print(i,j) i.e 4 2 checks j==3  i.e 2==3 false j became incremented from 2 to 3
i=4,j=3 checks 3<6 True so print(i,j) i.e 4 3 checks j==3  i.e 3==3 True so terminated inner loop but nothing happens to outer loop.means outer loop became incremented
i is incremented from 4 to 5


i=5 checks 5<6 True then enter into outer loop
i=5,j=1 checks 1<6 True so print(i,j) i.e 5 1 checks j==3  i.e 1==3 false j became incremented from 1 to 2 
i=5,j=2 checks 2<6 True so print(i,j) i.e 5 2 checks j==3  i.e 2==3 false j became incremented from 2 to 3
i=5,j=3 checks 3<6 True so print(i,j) i.e 5 3 checks j==3  i.e 3==3 True so terminated inner loop but nothing happens to outer loop.means outer loop became incremented
i is incremented from 5 to 6

i=6 checks 6>6 False come out from the loop no more further iterations.

