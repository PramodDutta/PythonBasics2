def greet(name):
    print("Hello",name)


class Person:
    def __init__(self,name):
        self.name = name

    def intro(self):
        print(self.name)