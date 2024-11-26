09:33 23-09-2024#animal-dog
class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def display_animal_details(self):
        print('animal name is',self.name)
        print('animal sounds like',self.sound)
    def animal_sound(self):
        print(f'{self.name} sounds as {self.sound}')
class Dog(Animal):
    def __init__(self,name,breed,sound):
        super().__init__(name,sound)
        self.sound='bow bow'
        self.breed=breed
    def display_animal_details(self):
        super.display_method_details()
        print('dogs breead is',self.breed)
    def dog_sound(self):
        super.animal_sound()
puppy=Dog('puppy','boxer','bow bow')
puppy.breed()
        
