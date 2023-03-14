# Abstract classes _____________________________________

# prevent a user from making an object of that class

# have to import this to use abstract method
from abc import ABC, abstractmethod

#     This is how you make the class abstract, also cant use this class because it is abstract
class Vehicle(ABC):

    @abstractmethod # <- has a methods but no implementation
    def go(self):
        pass

    @abstractmethod # <-
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car in drive")

    def stop(self):
        print("This car stoped")

class Motocykle(Vehicle):
    def go(self):
        print("Motocykle in drive")

    def stop(self):
        print("This motorcycle stoped")


car_1 = Car()
car_1.go()

motor = Motocykle()
motor.go()

car_1.stop()
motor.stop()

# vehicle = Vehicle() <- you cannot do this because this is abstract