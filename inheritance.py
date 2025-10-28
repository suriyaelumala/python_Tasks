# Inheritance in Python
# This shows how one class can inherit from another.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (inherits from Animal)
class Dog(Animal):
    def speak(self):  # Override method
        print(f"{self.name} barks.")

# Create objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

animal.speak()  # Outputs: Generic Animal makes a sound.
dog.speak()     # Outputs: Buddy barks.