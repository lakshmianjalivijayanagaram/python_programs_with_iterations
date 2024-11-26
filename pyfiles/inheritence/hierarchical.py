class Animal():
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print(f'{self.name} makes sound')
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f'{self.name} sounds like bow bow')
class cat(Animal):
    def __init__(self,name):
        self.name=name
    def meow(self):
        print(f'{self.name} sounds like meow meow')
dog=Dog('puppy')
dog.bark()
print(dog.name)
cat=cat('snoopy')
cat.meow()
print(cat.name)
