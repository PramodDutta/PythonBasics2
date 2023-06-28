class A:
    def __init__(self):
        pass

    def __init(self,a):
        pass #Nothing

    def __init(self,a,b):
        pass

    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C(A, B):
    pass

class D(B, A):
    pass

obj1 = C()
obj1.greet()

obj2 = D()
obj2.greet()

print(C.mro())
print(D.mro())