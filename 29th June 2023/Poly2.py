# Overriding

class Animal:
    def sound(self):
        print("Animal Sound")


class Dog(Animal):
    def sound(self):
        print("Dog Sound")


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()


# OverLoading

class MathUtil:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c, d):
        return a + b + c + d


math = MathUtil()
math.add(1, 2)
math.add(1, 2, 3)

# Python does not support method overloading directly like some other languages (e.g., Java),

