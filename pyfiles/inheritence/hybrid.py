class vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def start(self):
        print(f'{self.name} is started')
class car(vehicle):
    def __init__(self,name,model):
        super().__init__(name,model)
    def drive(self):
        super().start()
class Truck(vehicle):
    def __init__(self,name,model):
        super().__init__(name,model)
    def drive(self):
        super().start()
class Electriccar(car):
    def __init__(self,name,model):
        super().__init__(name,model)
    def charged(self):
        print(f'{self.name} is filled charging')
ecar=Electriccar('kia','784')
print(Electriccar.mro())
ecar.charged()
print(ecar.name)
print(ecar.model)
