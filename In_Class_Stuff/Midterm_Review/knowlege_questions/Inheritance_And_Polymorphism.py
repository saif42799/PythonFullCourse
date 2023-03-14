# Inheritance and Polymorphism___________________________


# Inheritance
# Allows us to create new classes known as "child classes" based
# off an existing class know as a "Parent class"

# The child class will inherit the attributes of the parent class

# parent class
# This includes subclass - one class inherits all other classes


# parent class
class Dog:
    dog = "shitzu"
    age = 8
    friendliness = 2
    eyecolor = "Blue"

    def __init__(self, name, age, friendliness, eyecolor):
        self.name = name
        self.age = age
        self.friendliness = friendliness
        self.eyecolor = "Brown"

    def likes_walks(self):
        return True

    #poly
    def bark(self):
        return "woof!"


# child class
class Huskey(Dog):
    def __init__(self, name, age, friendliness, eyecolor):
        # calls the super class ^
        super().__init__(name, age, friendliness, eyecolor)

        # polymorphism
    def bark(self):
        return "woooo wooooo!"

class GoldernRetriver(Dog):
    def __init__(self, name, age, friendliness, eyecolor):
        super().__init__(name, age, friendliness, eyecolor)

    # polymorphism
    def bark(self):
        return "cough cough!"


sammy = Huskey('Sammy', 2, 10, " ")
print(sammy.name, " | Age:", sammy.age, " | Friendliness: ",sammy.friendliness, " | Eye color: ",sammy.eyecolor)
print(sammy.likes_walks())
print(sammy.name, sammy.bark())

print(

)
#poly
golden = GoldernRetriver('Bob', 6, 8, " ")
print(golden.name, " | Age:", golden.age, " | Friendliness: ",golden.friendliness, " | Eye color: ",golden.eyecolor)
print(golden.name, golden.bark())


print()
# Polymorphism___________________________
# can take multiple forms
# A child class that inherits a function from the parent class can override
# that function and give that function new rules to follow
