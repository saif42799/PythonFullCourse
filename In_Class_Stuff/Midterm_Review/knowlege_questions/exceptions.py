# Exception ------------------------------------------------------
# is an object with a description of what went wrong and a tracback of where the problem accru ed
#ex
try:
    print(0 / 0)
except ZeroDivisionError:           # many types of exceptions
    print("cannot divide by zero")

try:
    print(0/0)
except:
    print("No no no, not in my house ")