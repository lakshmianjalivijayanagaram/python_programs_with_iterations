'''print('main starts')
l=[11,22,44]
try:
    print('try strarts')
    ip=int(input('enter index position'))
    print(l[ip])
    print('a')
    print('try ended')
except IndexError as ie:
    print(ie)
except NameError as ne:
    print(ne)
print('main end')'''
'''
l=[10,20,30]
try:
    ip=int(input('enter index position'))
    print(l[ip])
    print(a)
except Exception as e:
    print(e)

print('main started')
try:
    print('try started')
    num1=int(input())
    num2=int(input())
    res=num1/num2
    print('try ended')
except Exception as e:
    print(e)
else:
    print(res)
finally:
    print('finally is getting executing')
print('main ends')


try:
    print('outer try is started')
    print(a)
    try:
        print('inner try is started')
        print(10/2)
        print('innr try is ended')
    except Exception as e:
        print(e)
except Exception as E:
    print(E)

try:
    fo=open('hello4.txt','x')
    try:
        data=eval(input('enter data'))
        fo.write(data)
        #print(fo.read())
    except Exception as e:
        print(e)
    finally:
        fo.close()
except Exception as e:
    print(e)





try:
    fo=open('haiijj.txt','x')
    try:
        val=eval(input('enter value'))
        fo.write(eval)
        #print(fo.read())
    except Exception as e:
        print(e)
    finally:
        fo.close()
        
except Exception as e:
    print(e)


try:
    a=int(input('enter num'))
    b=int(input('enter num'))
    if b==0:
        raise ZeroDivisionError('we cant devide')
except Exception as E:
    print(E)


class DemoError(BaseException):
    def __init__(self,msg):
        self.msg=msg

try:
    raise DemoError('user raised this error')
except DemoError as d:
    print(d)
print('main is ended')


def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
f2()

def f1():
    print('f1 is started')
    try:
        a=10/0
    except Exception as e:
        print(e)
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
f2()   

def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')
def f2():
    print('f2 is sterted')
    try:
        f1()
    except Exception as e:
        print(e)
    print('f2 is ended')
f2()
'''
def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
try:
    f2()
except Exception as e:
    print(e)
print('main ends')





    

    







        




        














        











        





        







    

