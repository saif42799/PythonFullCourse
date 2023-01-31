
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + " cm tall")


number_one = int(input("Enter a number: "))
number_two = int(input("Enter a second number: "))

sum = number_one + number_two

print("Sum: " + str(sum))


#another way to write user input

print('Enter your name: ')
user_name = input()
print('Hello, ' + user_name)