'''class A:
    x=100
    _y=999
    __z=10
    @classmethod
    def get_pd(cls):
        print(cls.__z)
    def display(self):
        print('display is public method')
    def _show(self):
        print('show is protected method')
    def __secured(self):
        print('secured is private method')
print(A.x)
print(A._y)
oa=A()
oa.display()
oa._show()
print(A._A__z)
oa._A__secured()
'''
class A:
    x=10
    _y=999
    __z=1000
    def display(self):
        print('public method is display')
    def _show(self):
        print('protected method is show')
    def __secured(self):
        print('secured method is secured')
print(A.x)
print(A._y)
print(A._A__z)
oa=A()
oa.display()
oa._show()
oa._A__secured()












              
