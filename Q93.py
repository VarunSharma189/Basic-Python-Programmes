# WAP in python to demonstrate the concept of Polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Making the animals speak
make_animal_speak(dog)  
make_animal_speak(cat)  
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")