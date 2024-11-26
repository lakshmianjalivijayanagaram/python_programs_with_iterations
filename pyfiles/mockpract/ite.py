'''
#BUILTIN ITERATORS
io=iter('hai')
print(next(io))
print(next(io))
print(next(io))
print(next(io))
#USERDEFINED ITERATORS
class CIRC:
    def __init__(self,sv,ev,up=1):
        self.sv=sv
        self.ev=ev
        self.updation=up
    def __iter__(self):
        print('__iter__ is called')
        self.i=self.sv
        return self
    def __next__(self):
        print(' __next__ is called')
        if self.i<self.ev:
            res=self.i
            self.i+=self.updation
            return res
        else:
            raise StopIteration
CIO=CIRC(1,10,1)
for i in CIO:
    print(i)
class QIRC:
    def __init__(self,sv,ev,up=1):
        self.sv=sv
        self.ev=ev
        self.updation=up
    def __iter__(self):
        print('__iter__is printing')
        self.i=self.sv
        return self
    def __next__(self):
        print('__nxt__ is printing')
        if self.i<self.ev+1:
            res=self.i**3
            self.i+=self.updation
            return res
        else:
            raise StopIteration
QIO=QIRC(1,5,1)
for i in QIO:
    print(i)


class fibo():
    def __init__(self,fv,sv,n):
        self.fv=fv
        self.sv=sv
        self.n=n
    def __iter__(self):
        self.ll=1
        return self
    def __next__(self):
        if self.ll<=self.n:
            self.ll+=1
            res=self.fv
            self.fv=self.sv
            self.sv=res+self.fv
            return res
        else:
            raise StopIteration
fiboo=fibo(1,2,10)
for i in fiboo:
    print(i)

'''
        







        











