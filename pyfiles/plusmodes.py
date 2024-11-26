#w+mode write after read
fo=open('dataa.txt','w+')
s='this is wplus mode'
fo.write(s)
fo.seek(0)
a=fo.readline()
print(a)
fo.close()
