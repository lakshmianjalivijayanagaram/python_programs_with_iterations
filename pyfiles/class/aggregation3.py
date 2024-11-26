class car:
    def __init__(self,cn,cmn,cc):
        self.cname=cn
        self.cmodelno=cmn
        self.ccolor=cc
    def car_start(self):
        print('car has started')
    def car_accelerated(self):
        print('car has accelerated')
    def car_stop(self):
        print('car has stoped')
class driver:
    def __init__(self,dn,did,da):
        self.dname=dn
        self.did=did
        self.dage=da
        cn=input('enter car name')
        cm=int(input('enter car model no '))
        cc=input('enter car color')
        CarObj=car(cn,cm,cc)
        self.dcar=CarObj

    def car_driving(self):
        print('driver enter into the car')
        self.dcar.car_start()
        self.dcar.car_accelerated()
        self.dcar.car_stop()
        print('driver come out from the car')
drive=driver('abcd',1234,40)
drive.car_driving()
print(drive.dcar)

        
        
