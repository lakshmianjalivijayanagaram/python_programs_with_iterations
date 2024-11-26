'''def anjali():
    print("hai hello")
anjali()#functions statements executed
print(anjali)#adrees we will get

#1.without arguments and without return type
def add():
    print(10+20)
add()

#1.mandatory arguments
def add(a,b):
    print(a+b)
add(10,20)
#2.keyword arguments
def add(a,b):
    print(a+b)
add(b=11,a=12)
#defining only positional arguments
def add(a,b,c,/):
    print(a+b+c)
add(10,20,2)
#defining only keyword arguments
def add(*,a,b):
    print(a+b)
add(a=10,b=115)

#3.default arguments
def add(a=10,b=11):
    print(a+b)
add(10,111)
#4.variable length arguments
def add(*args):
    print(args)
    print(type(args))
    summ=0
    for i in args:
        summ+=i
    print(summ)
add(10,20,30,40)
#5.variable length keyword arguments
def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
add(a=1,b=2,c=3,d=4)
def fun(a,b,c=10,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
fun(1,2,3,11,22,33,44,name='anjali',cla='python')

#3.without arguments and with return type
def function():
    if 5>2:
        return 89
    elif 55>5:
        return 'hai'
    else:
        return 10,'hai',222
    
print(function())
a=function()
print(a)
if 111111>function():
    print(100)
else:
    print(10000)
#function with arguments and with return type
def add(a,b):
    return a+b
print(add(10,20))
def add():
    return
print(add())

#with arguments and without reurn type
def add(a,b):
    print(a+b)
add(10,20)
'''


    


    
    
