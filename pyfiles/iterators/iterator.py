'''class QIRC():
    def __init__(self,sv,fv,up=1):
        self.sv=sv
        self.fv=fv
        self.up=up
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i<self.fv:
            res=self.i**3
            self.i+=self.up
            return res
        else:
            raise StopIteration
qo=QIRC(1,5)
for i in qo:
    print(i)'''
class fibo():
    def __init__(self,fv,sv,n):
        self.fv=fv
        self.sv=sv
        self.n=n
    def __iter__(self):
        self.i=1
        return self
    
    def __next__(self):
        if self.i<self.n:
            self.i+=1
            res=self.fv
            self.fv=self.sv
            self.sv=res+self.sv
            return res
        else:
            raise StopIteration
fo=fibo(1,2,10)
for i in fo:
    print(i)
















'''class CIRC():
    def __init__(self,sv,ev,up):
        self.sv=sv
        self.ev=ev
        self.up=up
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i<self.ev:
            res=self.i
            self.i+=self.up
            return res
        else:
            raise StopIteration
CIO=CIRC(1,5,1)
for i in CIO:
    print(i)'''

