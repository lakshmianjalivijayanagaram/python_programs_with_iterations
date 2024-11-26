class address:
    def __init__(self,d,st,co):
        self.district=d
        self.state=st
        self.country=co
    def display_address(self):
        print('district is',self.district)
        print('state is',self.state)
        print('country is',self.country)
class student:
    def __init__(self,sn,sa,sc):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        d=input('enter district')
        st=input('enter state')
        co=input("enter country")
        Adressobject=address(d,st,co)
        self.saddress=Adressobject
    def student_details(self):
        print('student name is',self.sname)
        print('student age is',self.sage)
        print('student class is',self.sclass)
        print('student address is',)
        self.saddress.display_address()
anjali=student('anjali',21,'python')
anjali.student_details()
        
