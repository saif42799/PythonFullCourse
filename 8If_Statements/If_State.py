#if statements = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 180:
    print("You are old!")
elif age >=10:
    print("You are an adult!")
elif age < 0:
    print("You havent been born yet!")
else:
    print("You are a child!")