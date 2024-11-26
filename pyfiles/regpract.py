import re
'''s='hai pythan'
#print(re.match('h',s))
#print(re.search('z',s))
#print(re.findall('v',s))

io=re.finditer('a',s)
for i in io:
    print(i)
print(re.findall('.',s))
print(re.findall('^h',s))
print(re.findall('n$',s))
a='hai hep hp heep hello'
print(re.findall('hep',a))
print(re.findall('he*p',a))
print(re.findall('he+p',a))
print(re.findall('he?p',a))
print(re.findall('he{1,2}p',a))
print(re.findall('he{1,3}p|hai',a))
'''
s='abc hai bye'
print(re.findall('[abc]',s))
print(re.findall('/W',s))
#print(re.findall('\w',s))
