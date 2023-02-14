# Control Flow
# Loops with break and continue

# if statements
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"


# if-then-else on one line
j = 10
parity = "even" if j % 2 == 0 else "odd"


# While loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# for and in loop
# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")

# loop with continue and break
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print(x)
 # Output 0, 1, 2 , 4




