with open('hai.txt','r') as fo:
    data=fo.read()
    op=data.split()
    maxiw=op[0]
    for i in op:
        if len(i)>len(maxiw):
            maxiw=i
    print(maxiw)
    print(type(op))
