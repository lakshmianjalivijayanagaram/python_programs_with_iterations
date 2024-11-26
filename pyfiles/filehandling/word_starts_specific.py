with open('hai.txt','r') as fo:
    data=fo.read()
    op=data.split()
    count=0
    for i in op:
        if i.startswith('h'):
            count+=1
            print(i)
    print(count)
    print(type(op))
