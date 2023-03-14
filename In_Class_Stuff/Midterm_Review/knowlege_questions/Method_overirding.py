
class Animal:

    def eat(self):
        print("Nom Nom")

class Rabbit(Animal):
    # this is overriding a method that is already defines in the parent class
    def eat(self):
        print("blah rabbit pellets")


rabbit = Rabbit()
rabbit.eat()