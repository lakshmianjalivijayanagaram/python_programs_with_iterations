with open('hai.txt','r') as fo:
    data=fo.read()
    op=data.split()
    count=0
    for i in op:
        count+=1
    print(count)
    print(data)
    print(type(data))
