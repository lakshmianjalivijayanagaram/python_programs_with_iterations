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
    def __init__(self,sn,sa,scl):
        self.sname=sn
        self.sage=sa
        self.sclass=scl
        area=input('enter area')
        city=input('enter city')
        state=input('enter state')
        ACO=Address(area,city,state)
        self.saddress=ACO
    def display_student_info(self):
        print('student name is',self.sname)
        print('student age is',self.sage)
        print('student sclass is',self.sclass)
        print('student address is')
        self.saddress.display_address()

deepsika=student('deepsika',22,'python')
deepsika.display_student_info()
shyam=student('shyam',23,'python')
shyam.display_student_info()
