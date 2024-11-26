'''class Address():
    def __init__(self,area,city,state):
        self.area=area
        self.city=city
        self.state=state
    def display_address(self):
        print('the area is',self.area)
        print('the city is',self.city)
        print('the state is ',self.state)
class Student():
    def __init__(self,sn,sa,scl,addr):
        self.sname=sn
        self.sage=sa
        self.sclass=scl
        self.addr=addr
    def disply_student_info(self):
        print('student name',self.sname)
        print('student age is',self.sage)
        print('student class is',self.sclass)
        print('student address is',end='')
        self.addr.display_address()
        #self.addr=bangloreobj
bangloreobj=Address('oa','banglore','karnataka')
so=Student('anjali',21,'python',bangloreobj)
so.disply_student_info()

class Address():
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_address(self):
        print('city name is',self.city)
        print('state name is',self.state)
        print('country name is',self.country)
class Student():
    def __init__(self,sn,sa,sc):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        c=input('enter city')
        s=input('enter state')
        co=input('enter country')
        aco=Address(c,s,co)
        self.saddr=aco
    def student_display_info(self):
        print('student name',self.sname)
        print('student age is',self.sage)
        print('student class is',self.sclass)
        print('student address is',end='')
        self.saddr.display_address()
so=Student('anjali',21,'python')
so.student_display_info()
'''
class Car():
    def __init__(self,cn,cmn,cc):
        self.cname=cn
        self.cmodelno=cmn
        self.ccolor=cc
    def car_start(self):
        print('car has strted')
    def car_accelerate(self):
        print('car is accelerated')
    def car_stop(self):
        print('car is stopped')
class Driver():
    def __init__(self,dn,di,da):
        self.dname=dn
        self.did=di
        self.dage=da
        cn=input()
        cmn=int(input())
        cc=input()
        co=Car('abcd',1234,'black')
        self.dcar=co
    def driving(self):
        print('driver eneter into the car')
        self.dcar.car_start()
        self.dcar.car_accelerate()
        self.dcar.car_stop()
        print('driver came out from car')
do=Driver('abhbnbhcd',1234,22)
do.driving()






















        
























              
