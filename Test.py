
ticket = input()

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[-1]) + int(ticket[-2]) + int(ticket[-3])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")





wage = 28
hours = 40
weeks = 52
salary = wage + hours + weeks

print('Salary is: ', salary)


birds=['sparrow', 'crow', 'eagle']

for x in birds:
    print(x)








