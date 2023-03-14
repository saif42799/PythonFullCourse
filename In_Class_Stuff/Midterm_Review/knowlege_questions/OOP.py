# OOP ------------------------------------------------------

# Four principles of OOP
# - inheritance
# - polymorphism
# - encapsulation
# - abstraction

# magic methods
# ex __init__
#    __str__

# define a class
class Car:

    # class attributes
    list_of_cars = []

    # constructor  (parameters)
    def __init__(self, make, model, year, color):

        # instance attributes
        self.make = make
        self.model= model
        self.year = year
        self.color = color
        Car.list_of_cars.append(self)

    # method
    def car_in_use(self):
        print("Car make: " + self.make + " | Car year: " + str(self.year))

    # magic method(dunder) print default string instead of jibergaber (Nicely prints out string of the object)
    def __str__(self):
        return self.make + " " + self.model + " (" + self.color + ")"

    # magic method(dunder) print default string instead of jibergaber (Strings representation of the object)
    def __repr__(self):
        return f"Car({self.color, ' Color of car'})"


# Object
car_1 = Car("Toyota", "Supra", 1997, "Red")

car_1.car_in_use()

print(car_1)










