'''class A:
    x=100
    _y=1000
    __z=10000
    @classmethod
    def get_pd(cls):#private can be accessed within the class so accessed inside the class
        print(cls.__z)
    def publicc(self):
        print('is is publicmethod')
    def _protectedd(self):
        print('it is protected method')
    def __private(self):
        print('private method it s')
ao=A()
print(ao.x)
print(ao._y)
#print(ao.__z)
ao.get_pd()
ao.publicc()
ao._protectedd()
ao._A__private()
'''
#magicmethods'
class book:
    def __init__(self,n,au,p):
        self.name=n
        self.author=au
        self.price=p
    def __str__(self):
        return self.name+" "+self.author
    def __del__(self):
        print(self,'is deleted')
python=book('python','gvn',9999)
django=book('django','shv',99999)
print(python)
del python
