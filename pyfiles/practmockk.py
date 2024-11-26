'''class cirf():
    def __init__(self,ll,ul,up):
        self.ll=ll
        self.ul=ul
        self.up=up
    def __iter__(self):
        self.i=self.ll
        return self
    def __next__(self):
        if self.i<self.ul:
            res=self.i
            self.i+=self.up
            return res
        else:
            raise StopIteration
        
ci=cirf(1,10,1)
for i in ci:
    print(i)'''
'''
l=[11,22,111]
try:
    print('a')
    ip=int(input())
    print(l[ip])
except IndexError as ie:
    print(ie)
except NameError as ne:
    print(ne)
  
#default exception block
l=[1,2,3]
try:
    print('a')
    ip=int(input())
    print(l[ip])
except:
    print('error handles')
#except NameError as Ne:
#    print(Ne)
#generic exception bloack
l=[1,2,3]
try:
    print(a)
    ip=int(input())
    print(l[ip])
except Exception as e:
    print(e)

l=[1,2,3]
try:
    print('a')
    num1=int(input())
    num2=int(input())
    print(num1/num2)
except Exception as e:
    print(e)
else:
    print('program done')
finally:
    print('using finally')

try:
    print('a')
    try:
        print(0/0)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

try:
    fo=open('aaa.txt','x')
    try:
        data=eval(input())
        fo.write(data)
        print(fo.read())
    except Exception as e:
        print(e)
except Exception as e:
    print(e)


try:
    fo=open('hhh.txt','x')
    try:
        data=eval(input())
        fo.write(data)
    except Exception as e:
        print(e)
except Exception as e:
        print(e)        


try:
    a=int(input())
    b=int(input())
    if b==0:
        raise ZeroDivisionError('we cannot devide')
except Exception as e:
    print(e)

else:
    print(a/b)


class DemoError(BaseException):
    def __init__(self,msg):
        self.msg=msg
try:
    raise DemoError('user raised error')
except DemoError as D:
    print(D)


class DemoError(BaseException):
    def __init__(self,msg):
        self.msg=msg
try:
    raise DemoError('user raised this error')
except DemoError as d:
    print(d)



def f1():
    a=10/0
def f2():
    f1()
f2()

def f1():
    
    print(10/0)
def f2():
    f1()
f2()

def f1():
    print('f1 start')
    print(10/0)
    print('f1 end')
def f2():
    print('f2 start')
    f1()
    print('f2 end')
f2()

def f1():
    print('f1 start')
    print(10/0)
    print('f1 end')
def f2():
    print('f2 start')
    f1()
    print('f2 end')
try:
    f2()
except Exception as e:
    print(e)

def f1():
    print('f1 start')
    print(10/0)
    print('f1 end')
def f2():
    print('f2 start')
    try:
        f1()
    except Exception as e:
        print(e)
    print('f2 end')
f2()


def f1():
    print('f1 start')
    print(10/0)
    print('f1 end')
def f2():
    print('f2 start')
    

class PinError(BaseException):
    def __init__(self,msg):
        self.msg=msg
class BalError(BaseException):
    def __init__(self,msg):
        self.msg=msg
class Bank:
    Bank_name='Sbi'
    bank_ifsc=1343
    def __init__(self,cn,cbal,pin):
        self.cname=cn
        self.cbal=cbal
        self.pin=pin
    def withdraw(self):
        try:
            epin=int(input())
            if self.pin!=epin:
                raise PinError('pin is wrong')
            try:
                bal=int(input())
            
                if self.cbal<bal:
                    raise BalError('insufficient balance')
            except BalError as b:
                print(b)
            else:
                self.cbal-=bal
        except PinError as p:
            print(p)
        else:
            print(self.cbal)
anjali=Bank('anjali',10000,1234)
anjali.withdraw()

class PinError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class BalError(BaseException):
    def __init__(self,msg):
        self.msg=msg
class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    def __init__(self,cname,cbal,pin):
        self.cname=cname
        self.bal=cbal
        self.pin=pin
    def withdraw(self):
        try:
            pin=int(input())
            if pin!=self.pin:
                raise PinError('pin wrong')
            try:
                bal=int(input())
                if bal>self.bal:
                    raise BalError('insufficient bal')
            except BalError as b:
                print(b)
            else:
                self.bal-=bal
                print('bal is ',self.bal)
        except PinError as pe:
            print(pe)
        
anju=Bank('anjali',1000,1234)
anju.withdraw()

'''



















        






















    
    

















    
















    





















        










    



