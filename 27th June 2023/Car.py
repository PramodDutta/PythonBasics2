# Class and Object - Car
# DM - name, color, model_name
# Method - start_engine, drive

# Tesla , Lambo

class Car:
    name = None
    color = None
    model_name = None

    def __init__(self, car_name, car_color, car_model_name):
        self.name = car_name
        self.color = car_color
        self.model_name = car_model_name

    def start_engine(self):
        print("Starting the engine -> " + self.name)

    def drive(self):  # Ref to the current Object
        print("Driving - > " + self.name)

    def print_all(self):
        print(self.name, self.model_name, self.color)


car_name = input("Enter Car name")
car_color = input("Enter Car Color")
car_model = input("Enter Car Model")

tesla = Car(car_name, car_color, car_model)  # Ref to the current Object

tesla.print_all()
tesla.start_engine()
tesla.drive()
tesla.name
