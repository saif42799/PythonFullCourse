import time
# for loop = a statement that will execute it's block of code
#            a limited amount of items

for i in range(10):
    print(i + 1)

print()

for i in range(50, 100 + 1):
    print(i)

print()
#counts up by 2
for i in range(50, 100 + 1, 2):
    print(i)

print()

for i in "Saif Shaikh":
    print(i)

print()

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")