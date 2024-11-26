for i in range(1,11):
    print(i)
    if i==5:
        break
    
print('*'*15)
for i in range(1,11):
   
    if i==5:
        break
    print(i)
print('*'*15)

a=1
while a<11:
    print(a)
    if a==5:
        break
    a=a+1
print('*'*15)
#continue examples
a=1
while a<11:
    
    if a==5:
        break
    print(a)
    a=a+1
print('*'*15)
for i in range(1,11):
    if i==5:
        continue
    print(i)
print('*'*15)
a=1
while a<11:
    if a==5:
        a=a+1
        continue
    print(a)
    a=a+1

