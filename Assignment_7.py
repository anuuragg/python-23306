# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Derived class inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method of each object
dog.speak()
cat.speak()
