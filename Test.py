wage = 28
hours = 40
weeks = 52
salary = wage + hours + weeks

num = 5
new_num = num + 1
starter_num = 0

while starter_num != new_num:
    print(str(starter_num) + " !")
    starter_num += 1




#___________________________
number = int(input())
word = input()

if number > 1 or number == 1 or number != 1:
    if word[-1] != "s" and number > 1:
        print(number, word + "s")
    if word[-1] == "s" and number > 1:
        print(number, word)
    if word[-1] == "s" and number == 1:
        print(number, word[0:-1])
    if word[-1] != "s" and number == 1:
        print(number, word)
    if word[-1] == "s" and number < 1:
        print(number,  word)
    if word[-1] != "s" and number < 1:
        print(number,  word + "s")
#___________________________



#___________________________
num = int(input())
num = str(num)
first_num = num[0]
print(first_num)
#___________________________


print('Salary is: ', salary)


birds=['sparrow', 'crow', 'eagle']

for x in birds:
    print(x)



a = 50
b = 5
c = 10

#a = 5
#b = 50
#c = 5

c = b
b = a
a = c

print(a)
print(b)
print(c)

print("Enter a number: ")
user_num = input()
# user enters 10
print(user_num + user_num)