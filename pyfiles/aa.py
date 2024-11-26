
'''def pro(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    if len(d)==1:
        return -1
    li=d.values()
    b=sorted(li,reverse=True)
    m=b[:len(b)]
    print(b)
    if len(b)==2 and b[-2]==b[-1]:
        return 1
    elif len(m)%2==0:
        for i in range(0,len(m),2):
           if m[i]==m[i+1]:
                continue
           else:
                return 0
    elif len(m)%2!=0:
        for i in range(0,len(m)-1,2):
            if m[i]==m[i+1]:
                print(i,i+1)
            else:
                print('aaaaaaaa')
        if m[-2]-1==m[-1]:
                #if m[-1]-1==b[-1]:
            print('hellllll')
        else:
            print('0 hell')
pro('xyyz')
'''
