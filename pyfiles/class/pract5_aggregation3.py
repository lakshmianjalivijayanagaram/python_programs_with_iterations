class car:
    def __init__(self,cn,cmn,cc):
        self.cname=cn
        self.cmodelno=cmn
        self.ccolor=cc
    def start(self):
        print('car is started')
    def accelerate(self):
        print('car is accelerated')
    def stop(self):
        print('car is stopped')
class driver:
    def __init__(self,dn,did,da):
        self.dname=dn
        self.did=did
        self.dage=da
        cn=input('enter carname')
        cmn=int(input('enter car model number'))
        cc=input("enter car color")
        carobject=car(cn,cmn,cc)
        self.car=carobject
    def driving(self):
        print('driver enter into the car')
        self.car.start()
        self.car.accelerate()
        self.car.stop()
        print('driver come out from the car')
pani=driver('pani',123,'black')
pani.driving()
