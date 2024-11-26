with open('hai.txt','r') as fo:
    data=fo.readlines()
    count=0
    for i in data:
        count+=1
    print(count)
    print(data)
    print(type(data))

