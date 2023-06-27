# Person


# Data Member

# Methods - Behav

class Person:
    name = None
    age = None
    email_id = None

    def __init__(self, name, age, email_id):
        self.name = name
        self.age = age
        self.email_id = email_id

    def sleep(self):
        print(self.name + " is Sleeping")

    def eating(self):
        print(self.name + " is Eating")


pramod = Person("Pramod","32","p@d.com") # Obj - 1
# pramod = Person() # Obj - 1
# pramod - ref , Person() - Object
print(pramod.name)
pramod.eating()
pramod.sleep()

amit = Person("Amit","32","a@b.com") # Obj - 2
amit.sleep()