from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Run"

class Bird(Animal):
    def sound(self):
        return "Chirp"

    def move(self):
        return "Fly"

def animal_behaviors(animal):
    print(f"The animal goes '{animal.sound()}' and it can {animal.move()}.")


dog = Dog()
bird = Bird()

animal_behaviors(dog)
animal_behaviors(bird)


