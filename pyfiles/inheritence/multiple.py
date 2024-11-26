class Teacher():
    def __init__(self,name,sub):
        self.name=name
        self.subject=sub
    def teach(self):
        print('teacher is teacing')
class Musician():
    def __init__(self,name):
        self.name=name
    def work(self):
        print('musician is practising music')
class person(Teacher,Musician):
    def __init__(self,name):
        self.name=name
    def my_details(self):
        print('i am ',self.name)
        print('i am working as teacher and i am interested to learning music')
anjali=person('anjali')
anjali.my_details()
