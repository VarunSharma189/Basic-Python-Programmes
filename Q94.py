# WAP in python to demonstrate the concept of Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog()
cat = Cat()

print(dog.speak())  
print(cat.speak())  
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")