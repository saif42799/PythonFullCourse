# Variables = a container for a value. Behaves as the value that it contains
# 10 = 5 + x
# x = 5

#String
firstName = 'Saif'
lastName = "Shaikh"
print("Your full name is: " + firstName + " " + lastName)

#type() prints the data type
print(type(firstName))

print("\n")

#int
age = 23
age = age + 1
# or
age += 1
print(age)
#to print a int and a string u would have to convert it (type casting)
print("Your age is: " + str(age))
print(type(age))

print("\n")

#float = floating point number (a decimal number)
height = 250.5
print("Your height is: " + str(height) + "cm")
print(type(height))

print("\n")

#Boolean
human = False
print("Are you a human? " + str(human))
print(type(human))
