# Recursion ------------------------------------------------------
# What is the advantage over loops?
#     Divide-and-conquer type problems
#     Tree search
#     Sorting
#     Elegant solution
#
# Limitations?
#     Less efficient
#     Can exhaust program stack


def sum_recursion(n):
    # base case
    if n == 0:
        return 0
    else:
        # general case
        return n + sum_recursion(n - 1)

print(sum_recursion(15))


# Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# a, b, c, d, e, f, g, h,  i,  j

# a + b = c : 0 + 1 = 1
# b + c = d : 1 + 1 = 2
# c + d = e : 1 + 2 = 3
# d + e = f : 2 + 3 = 5
# so on...


class Ques_2:

    def __init__(self, name):
        self.name = name

    def compare(self):
        my_name = "saif"

        if self.name == my_name:
            return 4
        else:
            return 0

flooe = Ques_2("Saif")
print(flooe.compare())


boo = True
while boo:
    try:
        userdata = str(input("Enter name: "))

        flooe2 = Ques_2(userdata)
        com = flooe2.compare()
        print(com)

        if com > 0:
            boo = False
        elif com == 0:
            print("Not the same name")
            boo = True
        else:
            boo = True


    except ValueError:
        print("Not the same name, try again.")




