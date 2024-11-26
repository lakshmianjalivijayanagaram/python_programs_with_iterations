 #while is inside for
#break inner loop using outer loop value
for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
    if j==3:
        break
    j=j+1
