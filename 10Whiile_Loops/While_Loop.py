#While loops = a statement that will execute its block of code as long
#              as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print("Hello " + name)

name_two = None

#nother way to write the while loop above
while not name_two:
    name_two = input("Enter your name: ")

print("Hello " + name_two)