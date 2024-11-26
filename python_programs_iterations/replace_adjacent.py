#10-07-2024
#Replacing even index elements to adject odd index elements
#i/p: [11,22,33,44,55,66]
#o/p: [22,11,44,33,66,55]

l=[11,22,33,44,55,66]
for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)

#PROCESS
"""
1.Given input is list
2.fetching each and every even index position of elements
  swapping even element with its adjacent element i.e odd index positioned element

i=1: fetching ip=0 and l[ip]=11
    l[ip],l[ip+1]=l[ip+1],l[ip]
    i.e l[ip]=11,l[ip+1] i.e l[1]=22 now l[0],l[1]=22,11 i.e l=[22,11,33,44,55,66]

i=2: fetching ip=2 and l[ip]=33
    l[ip],l[ip+1]=l[ip+1],l[ip]
    i.e l[ip]=11,l[ip+1] i.e l[3]=44 now l[0],l[1]=44,33 i.e l=[22,11,44,33,55,66]

i=2: fetching ip=4 and l[ip]=66
    l[ip],l[ip+1]=l[ip+1],l[ip]
    i.e l[ip]=11,l[ip+1] i.e l[5]=66 now l[0],l[1]=66,55 i.e l=[22,11,44,33,66,55]

3.After completion of all the iterations printing the output 
  i.e [22, 11, 44, 33, 66, 55]
