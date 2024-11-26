'''fo=open('data.txt','r')
print(fo.readlines())
fo.close()

with open('data.txt','r') as fo:
    a=fo.read()
    b=a.split()
    count=0
    for i in b:
        count+=1
    print(count)
    print(fo.name)
    print(fo.readable())
    print(fo.mode)
    print(fo.closed)
    print(fo.writable())
print(fo.closed)'''
with open('data.txt','r') as fo:
    b=fo.readlines()
    count=0
    for i in b:
        if len(i)>=30:
            count+=1
    print(count)
