class car:
    def __init__(self,cn,cmn,cc):
        self.cname=cn
        self.carmodelno=cmn
        self.ccolr=cc
    def start(self):
        print('car has started')
    def accelerate(self):
        print('car has accelerated')
    def stop(self):
        print('car has stopped')
class driver():
    def __init__(self,dn,did,da):
        self.dname=dn
        self.did=did
        self.dage=da
        cn=input('enter name')
        cmn=int(input("enter number"))
        cc=input("enter  car color")
        carobj=car(cn,cmn,cc)
        self.dcar=carobj
    def driving(self):
        print("driver enter into car")
        self.dcar.start()
        self.dcar.accelerate()
        self.dcar.stop()
anjali=driver('anjali',1234566,21)
anjali.driving()

              
