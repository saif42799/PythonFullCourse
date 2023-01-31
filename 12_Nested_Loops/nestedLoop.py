# nested loops = The "inner" will finish all of it's iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
colums = int(input("How many colums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="") # stops cursor from going to next line
    print()