#tv has a remote
#student has address
class address:
    def __init__(self,d,st,co):
        self.district=d
        self.state=st
        self.country=co
    def display_address(self):
        print(' district is',self.district)
        print(' state is',self.state)
        print('
              country is',self.country)
class student:
    def __init__(self,sn,sa,sc,saddr):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        self.saddress=saddr
    def student_details(self):
        print('student name is',self.sname)
        print('student age is',self.sage)
        print('student class is',self.sclass)
        print('student address is',end=" ")
        self.saddress.display_address()
apobject=address('kadapa','ap','india')
anjali=student('anjali',21,'python',apobject)
anusha=student('anusha',25,'python',apobject)
anjali.student_details()
anusha.student_details()
        
