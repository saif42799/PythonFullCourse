# dictionary section ------------------------------------------
#             Key     : Value
import document

hero_dict = {"Batman" : 1, "Superman" : 2, "Wonder Woman" : 3}

hero_rank_num = hero_dict["Superman"]
print("Ranked number: ", hero_rank_num)

# KeyError
try:
    hero_nonExsit = hero_dict["Owl man"]
except KeyError:
    print("Wrong universe")

# in
hero_member = "Batman" in hero_dict
print(hero_member)

hero_nonMemebr = "Bum man" in hero_dict
print(hero_nonMemebr)

# get method
wonder_out = hero_dict.get("Wonder Woman", 0)
print(wonder_out)

cat_in = hero_dict.get("Catwoman", 0)
print(cat_in)

# replace and add
hero_dict["Wonder Woman"] = 4

hero_dict["Catwoman"] = 3

print(hero_dict)


# defaultdict - idk

stuff = {"AmericanPythoninta"}
word_counts = {}
for i in stuff:
    if i in word_counts:
        word_counts[i] += 1
    else:
        word_counts[i] = 1

print(word_counts)


print()
# sets ---------------------------------------------

# empty set cannot look like this: empty_set = {} <- this would be a dictionary
#empty set
s = set()

s.add(1)
s.add(2)
s.add(3)

print(s)  # print in {}, {1, 2, 3}

length = len(s)
print(length)

y = 4 in s
print(y)

print("------")
# sets are faster than lists
# 1st: Use "in" on a set and it is faster than using on a list
# 2nd: You can find distink item in collections

#ex
item_list = [1,2,3,1,2,3]
print(item_list)

print(len(item_list))

set_list = set(item_list)
print(set_list)
print(len(set_list))

back_to_list = list(set_list)
print(back_to_list)



print()
# lists --------------------------------------------
# []
interger_list = [1, 2, 3, 4, 5]
hertero_list = ["String", 0.1, True]
lists_of_Lists = [interger_list, hertero_list, []]

# indexing in list
zero = interger_list[0]
print(zero)

last = interger_list[-1]
print(last)

# change index
interger_list[0] = -1
print(interger_list)

# check list membership using "in"
print(1 in [1, 2, 3, 4])

# "extend" or add to list
x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

j = [1, 2, 3]
y = j + [4, 5, 6]
print(y)

x.append(0)
print(x)


print()
# Tuple --------------------------------------------
# Anything you can do with list you can do to tuples but you CANNOT modify tuples
# Tuples use () or nothing at all
my_tuple = (1, 2, 3)
other_tuple = 1, 2, 3

# Multi assignment
x, y = 1, 2
print(x, "and", y)

x, y = y, x
print(x, "and", y)


print()
# Slicing --------------------------------------------

# slice with list
# [Start : Stop : End]
num_list = [1, 2, 3, 4, 5, 6]

start_list = num_list[2:]
print(start_list)

stop_list = num_list[:3]
print(stop_list)

stop_list2 = num_list[:-3]
print(stop_list2)

combo_list = num_list[0:5:2]
print(combo_list)

combo_list2 = num_list[::3]
print(combo_list2)

all_list = num_list[:]
print(all_list)



print()
# Exception ------------------------------------------------------
# is an object with a description of what went wrong and a tracback of where the problem accru ed
#ex
try:
    print(0 / 0)
except ZeroDivisionError:           # many types of exceptions
    print("cannot divide by zero")






print()
# Recursion ------------------------------------------------------






print()
# OOP ------------------------------------------------------






