with open('hai.txt','r') as fo:
    data=fo.read()
    op=data.split()
    li=[]
    for i in range(0,len(op)):
        if len(op[i])==10:
            li.append(op[i])
            #print(i)
    print(li)
    print(type(op))
