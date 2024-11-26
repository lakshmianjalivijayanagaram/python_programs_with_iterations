'''def isIsogram(s):
        #Your code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        li=list(d.values())
        li.sort()
        for i in li:
            if i>1:
                return 0
        return 1
print(isIsogram('machine'))

arr=[4,8,4,2,0,-10,7,3,-7]
def getPairs(arr):
        # code here
        a=[]
        arr.sort()
        print(arr)
        j=0
        i=len(arr)-1
        while j<i:
                if arr[j]+arr[i]<0:
                    print('hai a')
                    j+=1
                elif arr[j]+arr[i]>0:
                    print('hello a')
                    i-=1
                else:
                    b=[arr[j],arr[i]]
                    a.append(b)
                    j+=1
                    i-=1
        return a
print(getPairs(arr))'''

arr=[-1,0,9,1,7]
for i<len(arr):
        if -i in arr:
                print([i,-i])



















