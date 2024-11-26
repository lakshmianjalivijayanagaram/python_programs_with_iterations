'''
#first read then write
fo=open('dataa.txt','a+')
fo.write('hai hello this is aplus mode')
fo.seek(0)
rd=fo.read()
print(rd)
fo.close()

#first write then read
fo=open('dataa.txt','a+')
fo.seek(0)
rd=fo.readline()
print(rd)

 fo.write('hai this is second time aplus mode using')
fo.close()

#r+mode
fo=open('dataa.txt','r+')
fo.write('what happen')
rd=fo.read(10)
print(rd)
fo.close()
'''
fo=open('dataa.txt','r+')
#fo.seek(0)
rd=fo.read(15)
print(rd)
fo.write('this is last line')
fo.close()
