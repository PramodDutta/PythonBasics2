# Multilevel inheritance
# Vehicle - Car - Tesla
# is A - Car is Vehicle, Telsa is a Car

class Vehicle:
    def start_engine(self):
        print("Engine Started!")


class Car(Vehicle):
    def drive(self):
        print("Driving the Car")


class Tesla(Car):
    def race(self):
        print("Tesla Car")


my_car = Tesla()

my_car.start_engine()
my_car.drive()
my_car.race()

print(" ---------")
