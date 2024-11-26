#create object of another class in main space and use in current class
class Address:
    def __init__(self,area,city,state):
        self.area=area
        self.city=city
        self.state=state

    def display_address(self):
        print('the area is',self.area)
        print('the city is',self.city)
        print('the state is',self.state)
class student:
    def __init__(self,sn,sa,scl,saddr):
        self.sname=sn
        self.sage=sa
        self.sclass=scl
        self.saddress=saddr
    def display_student_info(self):
        print('student name is',self.sname)
        print('student age is',self.sage)
        print('student sclass is',self.sclass)
        print('student address is')
        self.saddress.display_address()
bangaloreobj=Address("OAR",'Banglore','karnataka')
s1=student("anjali",21,'python',bangaloreobj)
s1.display_student_info()
s2=student('rama',22,10,bangaloreobj)
s2.display_student_info()
