def pivotplace(list,first,last):
    pivot=list[first]
    left=first+1
    right=last
    while True:
        while left<=right and list[left]<=pivot:
            left=left+1
        while left<=right and list[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list[left],list[right]=list[right],list[left]
    pivot,list[right]=list[right],pivot
def quicksort(list,first,last):
    if first<last:
        p=pivotplace(list,first,last)
        quicksort(list,first,p-1)
        quicksort(list,p+1,last)

            
