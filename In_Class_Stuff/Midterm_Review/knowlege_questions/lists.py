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