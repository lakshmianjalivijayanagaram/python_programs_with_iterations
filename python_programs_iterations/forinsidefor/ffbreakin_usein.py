#for inside for
#break inner loop with inner loop value
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break

#process
1.for loop which is iterates for i=1,2,3,4,5
2.fetching i=1 get inside the inner for loop print and checks the value for every iteration if the condition is satisfies
now
i=1:    i=1 fetch j=1 print(1,1) i.e 1 1  checks j==3 i.e 1==3 False j is beacame iterated
        i=1 fetch j=2 print(1,2) i.e 1 2  checks j==3 i.e 2==3 False j is beacame iterated
        i=1 fetch j=3 print(1,3) i.e 1 3  checks j==3 i.e 3==3 True
        so inner loop became terminated but nothing is happend to outer loop so inner loop iterations stopped now went to outer loop
        
i=2:    i=2 fetch j=1 print(2,1) i.e 2 1  checks j==3 i.e 1==3 False j is beacame iterated
        i=2 fetch j=2 print(2,2) i.e 2 2  checks j==3 i.e 2==3 False j is beacame iterated
        i=2 fetch j=3 print(2,3) i.e 2 3  checks j==3 i.e 3==3 True
        so inner loop became terminated but nothing is happend to outer loop so inner loop iterations stopped now went to outer loop

i=3:    i=3 fetch j=1 print(3,1) i.e 3 1  checks j==3 i.e 1==3 False j is beacame iterated
        i=3 fetch j=2 print(3,2) i.e 3 2  checks j==3 i.e 2==3 False j is beacame iterated
        i=3 fetch j=3 print(3,3) i.e 3 3  checks j==3 i.e 3==3 True
        so inner loop became terminated but nothing is happend to outer loop so inner loop iterations stopped now went to outer loop

i=4:    i=4 fetch j=1 print(4,1) i.e 4 1  checks j==3 i.e 1==3 False j is beacame iterated
        i=4 fetch j=2 print(4,2) i.e 4 2  checks j==3 i.e 2==3 False j is beacame iterated
        i=4 fetch j=3 print(4,3) i.e 4 3  checks j==3 i.e 3==3 True
        so inner loop became terminated but nothing is happend to outer loop so inner loop iterations stopped now went to outer loop

i=5:    i=5 fetch j=1 print(5,1) i.e 5 1  checks j==3 i.e 1==3 False j is beacame iterated
        i=5 fetch j=2 print(5,2) i.e 5 2  checks j==3 i.e 2==3 False j is beacame iterated
        i=5 fetch j=3 print(5,3) i.e 5 3  checks j==3 i.e 3==3 True
        so inner loop became terminated but nothing is happend to outer loop so inner loop iterations stopped now went to outer loop
        
Now outer loop range has done so both inner& outer loop has done


