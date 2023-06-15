class Hello:
    name = None
    def __init__(self):
        print("Default Constructor called")
    def __init__(self,name):
        self.name = name
        print("Param Constructor called")
    def sayHello(self):
        print("Hello")


a = Hello("Pramod")
a.sayHello()