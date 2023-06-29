# Hierarchical Inheritance
# Hierarchical inheritance involves multiple derived
# classes inheriting from a single base class.

class Animal:
    def speak(self):
        print("Animal Speak")


class Dog(Animal):
    def bark(self):
        print("Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow!")


my_dog = Dog()
my_dog.speak()  # Inherited from Animal
my_dog.bark()  # Specific to Dog


my_cat = Cat()
my_cat.speak()  # Inherited from Animal
my_cat.meow()