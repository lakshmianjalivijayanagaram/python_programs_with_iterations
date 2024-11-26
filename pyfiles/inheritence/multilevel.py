#Device,Computer,laptop
class device():
    def __init__(self,name):
        self.name=name
    def power_on(self):
        print(f'{self.name} is power on')
class computer(device):
    def __init__(self,name,type):
        self.name=name
        self.devicetype=type
    def computer_type(self):
        print(f'{self.name} type is {self.devicetype}')
class laptop(computer):
    def __init__(self,name,type):
        self.name=name
        self.devicetype=type
    def portable(self):
        print(f'{self.name} type is {self.devicetype} and it is portable')
dell=laptop('dell','windows11')
dell.portable()
print(dell.devicetype)
