def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        leftlist=list[:mid]
        rightlist=list[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        i=0
        j=0
        k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list[k]=leftlist[i]
                k+=1
                i+=1
            else:
                list[k]=rightlist[j]
                k+=1
                j+=1
        while i<len(leftlist):
            list[k]=leftlist[i]
            k+=1
            i+=1
        while j<len(rightlist):
            list[k]=rightlist[j]
            k+=1
            j+=1
