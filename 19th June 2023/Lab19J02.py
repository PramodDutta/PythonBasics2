class Person:
    def __init__(self, name):
        self.name = name
        print("Hello")

    def greet(self):  # Method - Class - Methods are functions that are associated with an object or a class.
        print("Hello" + self.name)


person = Person("Alice")
person.greet()
print(person.name)


def greet2():  # Func - Functions are standalone blocks of code that perform a specific task
    print("Hello 2")


greet2()
